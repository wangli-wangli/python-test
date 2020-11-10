# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:13:55 2020

@author: lenovo
"""

import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt,data,file_data,unpack

@ddt
class TestBaidu(unittest.TestCase):
    '''百度搜索测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.base_url="https://www.baidu.com"
        
    def baidu_search(self,search_key):     
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)
        
     
    #参数化使用方式一
    @data(["case1","selenium"],["case2","ddt"],["case3","python"])
    @unpack
    def test_search1(self,case,search_key):
        print("第1组测试用例：",case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
        
      
    #参数化使用方式二
    @data(("case1","selenium"),("case2","ddt"),("case3","python"))
    @unpack
    def test_search2(self,case,search_key):
        print("第2组测试用例：",case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
        
    #参数化使用方式三
    @data({"search_key":"selenium"},{"search_key":"ddt"},{"search_key":"python"})
    @unpack
    def test_search3(self,search_key):
        print("第3组测试用例：",search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
        
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)
    
        
        
        