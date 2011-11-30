from twisted.trial import unittest

from readerd.instance import ReaderdService

class TestReaderd(unittest.TestCase):
    def test_initialization(self):
        rd = ReaderdService(
            db_url="sqlite:///:memory:",
            redis_host="localhost",
            redis_port=6379
        )

        # Dummy assertion
        self.assert_(rd)
