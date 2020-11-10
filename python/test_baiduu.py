# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:13:55 2020

@author: lenovo
"""

import unittest
from time import sleep
from selenium import webdriver

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpCalss(cls):
        cls.driver=webdriver.Chrome()
        cls.base_url="https://www.baidu.com"
        
    def test_search_key_selenium(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)
        title=self.driver.title
        
        
    def test_search_key_selenium(self):
        search_key="selenium"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,"selenium_百度搜索")
        
    def test_search_key_unittest(self):
        search_key="unittest"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,"selenium_百度搜索")
        
    @classmethod
    def tearDownCalss(cls):
        cls.driver.quit()
        
        
        