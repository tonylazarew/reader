from twisted.application import service

"""Readerd instance service implementation.
"""

class ReaderdService(service.Service):
    """The core service."""
    def __init__(self, db_url, redis_host, redis_port=6379):
        """Initialize the service instance.

        @param db_url: Database URL for consumption by SQLalchemy
        @type db_url: C{str}
        @param redis_host: Redis server host name
        @type redis_host: C{str}
        @param redis_port: Redis server port
        @type redis_port: C{int}
        """
        assert db_url and redis_host and redis_port

        self.config = {}
        self.config["db_url"] = db_url
        self.config["redis_host"] = redis_host
        self.config["redis_port"] = int(redis_port)
