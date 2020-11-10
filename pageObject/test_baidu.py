# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:03:24 2020

@author: lenovo
"""

import unittest
from time import sleep
from selenium import webdriver
from baidu_page2 import BaiduPage

class TestBaiduPage(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        
    def test_baidu_search_case(self):
        page=BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input="selenium"
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title(),"selenium_百度搜索")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
if __name__=='__main__':
    unittest.main()
        
        
        