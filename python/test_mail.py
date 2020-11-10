# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:55:39 2020

@author: lenovo
"""
from time import sleep
from selenium import webdriver
from module import Mail

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("http://www.126.com")
    #调用Mail类并接受driver驱动
    mail=Mail(driver)
    
    #登录
    mail.login()
    
    #登录之后的动作
    sleep(5)
    
    #退出
    mail.logout()
    
    driver.quit()
