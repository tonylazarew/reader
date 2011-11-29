from twisted.application import service
from twisted.plugin import getPlugins

import readerd.contentplugins
from readerd.interfaces import IContentPlugin

"""Feed service implementation.
"""

class Feed(service.MultiService):
    def __init__(self, readerd_service):
        service.MultiService.__init__(self)

        self.readerd_service = readerd_service
        self.plugins = {}

        self.createChildServices()

    def createChildServices(self):
        # Enable all the content plugins we find
        for plugin_obj in getPlugins(IContentPlugin, readerd.contentplugins):
            plugin_obj.initialize(self)
            self.plugins[plugin_obj.name] = plugin_obj
            plugin_obj.setServiceParent(self)
