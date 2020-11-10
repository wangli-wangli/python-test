# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:49:30 2020

@author: lenovo
"""

from selenium.webdriver import Remote,DesiredCapabilities
driver=Remote(desired_capabilities=DesiredCapabilities.CHROME.copy())
driver.get("http://www.baidu.com")

driver.quit()
