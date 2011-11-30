import imp
import os
import shutil
import sys

import mock
from twisted.internet import defer
from twisted.trial import unittest

from readerpr.daemon.feed import Feed

init_code = """
from twisted.plugin import pluginPackagePaths
__path__.extend(pluginPackagePaths(__name__))
__all__ = []
"""

plugins = {
    "dummy": """
from zope.interface import implements
from twisted.application import service
from twisted.plugin import IPlugin

from readerpr.daemon.interfaces import IContentPlugin

class DummyPlugin(service.Service):
    implements(IPlugin, IContentPlugin)

    name = "dummy"

    def initialize(self, feed):
        self.feed = feed

dummy_plugin = DummyPlugin()
""",
}

class TestContentPlugins(unittest.TestCase):
    """Test basic content plugins operations.
    """
    plugins_storage = "readerpr.daemon.contentplugins"

    def setUp(self):
        # Creating a plugin directory and adding some plugin code there
        os.mkdir("contentplugins")
        with open("contentplugins/__init__.py", "w") as f:
            f.write(init_code)
            f.flush()
            f.close()

        for name, code in plugins.items():
            with open("contentplugins/{}.py".format(name), "w") as f:
                f.write(code)
                f.flush()
                f.close()

        try:
            mod = imp.load_module(
                self.plugins_storage,
                *imp.find_module("contentplugins", [os.getcwd()])
            )
        except ImportError:
            return defer.fail()
        sys.modules[self.plugins_storage] = mod

    def tearDown(self):
        del(sys.modules[self.plugins_storage])
        shutil.rmtree("contentplugins")

    def test_pluginsEnabled(self):
        # Initializing the Feed object.  It should be enough to fire its
        # content plugin detection logic.
        feed = Feed(mock.Mock())
        for plugin in feed.plugins:
            self.assertIn(plugin, plugins.keys())
