# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:25:33 2020

@author: lenovo
"""

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()

#driver.quit()