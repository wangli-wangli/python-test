# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:52:23 2020

@author: lenovo
"""
from base import BasePage

class BaiduPage(BasePage):
    
    url="https://www.baidu.com"
        
    def search_input(self,search_key):
        self.by_id("kw").send_keys(search_key)
        
    def search_button(self):
        self.by_id("su").click()