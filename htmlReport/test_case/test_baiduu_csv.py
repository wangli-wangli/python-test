# -*- coding: utf-8 -*-

import unittest
from time import sleep
from selenium import webdriver
import csv
import codecs
from itertools import islice
from parameterized import parameterized

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
        
        
    def test_search(self):
        with codecs.open('./baidu_data.csv','r','utf_8_sig') as f:
            data=csv.reader(f)
            #islice:如果不等于 1 ，则进行读取操作
            for line in islice(data,1,None):
                search_key=line[1]
                self.baidu_search(search_key)
        
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)

    
        
        
        