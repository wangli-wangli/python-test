# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:45:29 2020

@author: lenovo
"""

class Mail:
    def __init__(self,driver):
        self.driver=driver
        
    def login(self,username,password):
        """登录"""
        login_frame=self.driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
        self.driver.switch_to.frame(login_frame)
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(username)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("dologin").click()
        
    def logout(self):
        """退出"""
        self.driver.find_element_by_link_text("退出").click()