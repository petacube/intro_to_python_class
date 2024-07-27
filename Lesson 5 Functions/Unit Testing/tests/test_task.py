import unittest

from task import func


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_func(self):
        self.assertEqual(func(3), 4, msg="adds 3 + 1 to equal 4")
    def test_func_bad(self):
        self.assertEqual(func(4), 5, msg="adds 4 + 1 to equal 5")

