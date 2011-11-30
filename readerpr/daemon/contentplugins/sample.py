from zope.interface import implements
from twisted.application import service
from twisted.plugin import IPlugin

from readerpr.daemon.interfaces import IContentPlugin

"""Sample implementation of content plugin.
"""

class SamplePlugin(service.Service):
    """Does nothing, just demonstrates how to write plugin code.
    """
    implements(IPlugin, IContentPlugin)

    name = "sample-plugin"

    def initialize(self, feed):
        self.feed = feed

# Twisted will use the object (not class) as a plugin and will return it to
# the Feed.  Thus the whole plugin can be disabled by just commenting out the
# following line:
sample_plugin = SamplePlugin()
