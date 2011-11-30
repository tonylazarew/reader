import os
from twisted.python import log

"""Instance configuration.
"""

tac_template = """# Twisted application configuration file for readerd.

# Database URL
db_url = "sqlite:///readerdb.sqlite"

# Redis connection parameters
redis_host = "localhost"
redis_port = 6379

import os
import sys
from twisted.application import service

# Do not modify this line
application = service.Application("readerd")

from readerpr.daemon import instance
readerd_svc = instance.ReaderdService(
    db_url=db_url, redis_host=redis_host, redis_port=redis_port)
readerd_svc.setServiceParent(application)

"""

def create(path):
    """Create an instance configuration."""
    readerd_tac_path = os.path.join(path, "readerd.tac")
    if os.path.isfile(readerd_tac_path):
        log.err("file already exists: {}".format(reader_tac_path))
        return 1

    with open(readerd_tac_path, "w") as tac:
        tac.write(tac_template)

    return 0
