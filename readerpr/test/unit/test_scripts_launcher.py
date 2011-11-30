import os
import shutil

from twisted.trial import unittest

from readerpr.daemon.scripts import config, launcher

class TestLaunchCommands(unittest.TestCase):
    """Test launch commands.
    """
    def setUp(self):
        self.path = os.path.join(os.getcwd(), "myreaderd")
        os.mkdir(self.path)

    def tearDown(self):
        shutil.rmtree(self.path)

    def test_startInEmptyDir(self):
        # Must fail, no readerd.tac exists
        self.assertEqual(launcher.start(self.path, _test=True), 1)

    def test_startCorrectly(self):
        config.create(self.path)
        self.assertEqual(launcher.start(self.path, _test=True), 0)
