from twisted.application import service
from twisted.plugin import getPlugins

from readerpr.daemon import contentplugins, interfaces

"""Feed service implementation.
"""

class Feed(service.MultiService):
    def __init__(self, daemon_service):
        service.MultiService.__init__(self)

        self.daemon_service = daemon_service
        self.plugins = {}

        self.createChildServices()

    def createChildServices(self):
        # Enable all the content plugins we find
        for plugin_obj in getPlugins(interfaces.IContentPlugin, contentplugins):
            plugin_obj.initialize(self)
            self.plugins[plugin_obj.name] = plugin_obj
            plugin_obj.setServiceParent(self)
