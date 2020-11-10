# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:34:03 2020

@author: lenovo
"""
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://m.baidu.com")

#参数数字为像素
print("设置浏览器宽480、高800显示")
driver.set_window_size(480,800)
driver.quit()

