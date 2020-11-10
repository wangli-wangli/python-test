# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:50:11 2020

@author: lenovo
"""

import unittest
from calculator import Calculator
class TestAdd(unittest.TestCase):
    """add()方法测试"""
    def test_add_integer(self):
        """整数相加"""
        c=Calculator(3,5)
        self.assertEqual(c.add(),8)
        
    def test_add_decimals(self):
        """小数相加"""
        c=Calculator(3.2,5.5)
        self.assertEqual(c.add(),8)
        
    def test_add_string(self):
        """字符串整数相加测试"""
        c=Calculator("7","9")
        self.assertEqual(c.add(),16)
        
if __name__=='__main__':
    unittest.main()