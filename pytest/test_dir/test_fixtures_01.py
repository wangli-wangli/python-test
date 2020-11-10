# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 00:03:45 2020

@author: lenovo
"""
import pytest
#功能函数
def multiply(a,b):
    return a*b

class TestMultiply:
    #==============Fixture=====================
    @classmethod
    def setup_class(cls):
        print("setup_class=========================>")
     
    @classmethod
    def teardown_class(cls):
        print("teardown_class=========================>")
        
    def setup_method(self,method):
        print("setup_method----------------->")
        
    def teardown_method(self,method):
        print("teardown_method--------------->")
        
    def setup(self):
        print("setup------------>")
    
    def teardown(self):
        print("teardown------------>")
    
    #=============测试用例========================
    def test_multiply_3_4(self):
          print('test_numners_3_4')
          assert multiply(3,4)==12
      
if __name__=='__main__':
    pytest.main()
   
    