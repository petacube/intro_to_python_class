import unittest

from task import sum


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sum(1, 2), 3, msg="adds 1 + 2 to equal 3")
    def test_zip(self):
        self.assertEqual(sum(1, 2), 3, msg="adds 1 + 2 to equal 3")
    def test_latitude(self):
        self.assertEqual(sum(1, 2), 3, msg="adds 1 + 2 to equal 3")
    def test_license_plate(self):
        self.assertEqual(sum(1, 2), 3, msg="adds 1 + 2 to equal 3")