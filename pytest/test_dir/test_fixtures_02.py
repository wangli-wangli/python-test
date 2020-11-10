# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 00:03:45 2020

@author: lenovo
"""
import pytest
#功能函数
def multiply(a,b):
    return a*b

#==============Fixture=====================
def setup_model(model):
    print("setup_model=========================>")
    
def teardown_model(model):
    print("teardown_model=========================>")
    
def setup_function(function):
    print("setup_function----------------->")
    
def teardown_function(function):
    print("teardown_function--------------->")
    
def setup():
    print("setup------------>")

def teardown():
    print("teardown------------>")
    
#=============测试用例========================
def test_multiply_3_4():
      print('test_numners_3_4')
      assert multiply(3,4)==12
      
if __name__=='__main__':
    pytest.main()
    #test_multiply_3_4()
    