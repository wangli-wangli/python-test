# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:55:39 2020

@author: lenovo
"""
from time import sleep
from selenium import webdriver
from module import Mail
import csv
import codecs
from itertools import islice
from xml.dom.minidom import parse
import json

def readTxt():
    #读取文件
    with(open("./data_file/usr_info.txt","r")) as user_file:
        data=user_file.readlines()
        
    #格式化处理
    users=[]
    for line in data:
        user=line[:-1].split(":")
        users.append(user)
        
    #打印users二位数组
    print(users)
    return users

def readCSV():
    
    #读取文件
    data=csv.reader(codecs.open('./data_file/usr_info.csv','r','utf-8-sig'))
        
    #格式化处理
    users=[]
    for line in islice(data,1,None):
        users.append(line)
        
    #打印users二位数组
    print(users)
    return users

def readXML():
    
    #打开XML文件
    dom=parse('./data_file/config.xml')
    
    #得到文档元素对象
    root=dom.getElement
    
    #获取（一组）标签
    tag_name=root.getElementsByTagName('platform')
    
    print(tag_name[0].firstChild.data)
    
def readJson():
    with open("./data_file/user_info.json","r") as f:
         data=f.read()
    
    user_list=json.loads(data)
    print(user_list)
     

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("http://www.126.com")
    
    
    
    #调用Mail类并接受driver驱动
    mail=Mail(driver)
    
    users=readTxt()
    
    #登录
    mail.login(users[0][0],users[0][1])
    
    #登录之后的动作
    sleep(5)
    
    #退出
    mail.logout()
    
    driver.quit()
