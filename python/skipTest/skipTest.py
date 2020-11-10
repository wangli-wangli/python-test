# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:05:34 2020

@author: lenovo
"""

import unittest

class MyTest(unittest.TestCase):
    
    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")
    
    @unittest.skipIf(3>2,"当条件为真时跳过测试")
    def test_skip_if(self):
        print("test bbb")
    
    @unittest.skipUnless(3>2,"条件为真时执行测试")
    def test_skip_unless(self):
        print("test ccc")
        
    @unittest.expectedFailure
    def test_skip_failure(self):
        self.assertEqual(2,3)
        
if __name__=='__main__':
    unittest.main()