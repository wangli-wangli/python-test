# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:55:57 2020

@author: lenovo
"""

import unittest

#定义测试用例的目的为当前目录中的test_case/目录
test_dir='./test_case'
suits=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir="F:/python/unittest_sample/test_case")

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suits)