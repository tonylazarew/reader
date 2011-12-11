from cyclone import web

"""Core web application code for webface.
"""

class WebfaceApplication(web.Application):
    """Application class for Cyclone."""
    def __init__(self):
        handlers = [
            (r"/", web.RequestHandler),
        ]
        settings = {}
        web.Application.__init__(self, handlers, **settings)

