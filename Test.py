#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Divsion import division

class TestSum1(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to division two numbers
        """
        a = 30
        b = 15
        result = division(a,b)
        self.assertEqual(result, 2)
        

class TestSum2(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to division two numbers
        """
        a = 40
        b = 8
        result = division(a,b)
        self.assertEqual(result, 5)
        
  

class TestSum3(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to division two numbers
        """
        a = 300
        b = 15
        result = division(a,b)
        self.assertEqual(result, 20)
        

class TestSum4(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to division two numbers
        """
        a = 35
        b = 7
        result = division(a,b)
        self.assertEqual(result, 20)
        
        
class TestSum5(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to division two numbers
        """
        a = 36
        b = 15
        result = division(a,b)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()
