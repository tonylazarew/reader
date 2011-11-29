from zope.interface import Interface, Attribute
from twisted.application import service

"""Interfaces for readerd classes.
"""

class IContentPlugin(Interface, service.IService):
    """Content plugin is responsible for polling and holding conversations with
    one or several social services (like RSS, Twitter, Facebook etc).
    """
    name = Attribute("name", "Name of the plugin")

    def initialize(feed):
        """This method is used by the Feed to initialize the content plugin.

        @param feed: Feed service instance
        @type feed: C{object}
        """
