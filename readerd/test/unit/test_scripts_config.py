import os
import shutil

from twisted.trial import unittest

from readerd.scripts import config

class TestCreate(unittest.TestCase):
    """Test 'create' command.
    """
    def setUp(self):
        self.path = os.path.join(os.getcwd(), "myreaderd")
        os.mkdir(self.path)

    def tearDown(self):
        shutil.rmtree(self.path)

    def test_create(self):
        config.create(self.path)
        self.assert_(os.path.isfile(os.path.join(self.path, "readerd.tac")))
