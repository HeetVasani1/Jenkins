#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Divsion import division

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to division two numbers
        """
        a = 30
        b = 15
        result = division(data)
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()
