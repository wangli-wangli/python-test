# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:40:22 2020

@author: lenovo
"""

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import yagmail

#把测试报告作为附件发送到指定邮箱
def send_mail(report):
    yag=yagmail.SMTP(user="wl15176128570@126.com",
                     password="HGDFAIMHMWDKQYWJ",
                     host="smtp.126.com")
    
    subject="主题，自动化测试报告"
    contents="正文，请查看附件"
    yag.send('15176128570@139.com',subject,contents,report)
    print("email has send out!")
    

#定义测试用例的目的为当前目录中的test_case/目录
test_dir='./test_case'
suits=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir="F:\python\htmlReport")

if __name__=='__main__':
    # 取当前日期时间
    now_time=time.strftime("%Y-%m-%d %H_%M_%S")
    html_report="./test_report/"+now_time+"result.html"
    fp=open("./test_report/"+now_time+"result.html","wb")
    runner=HTMLTestRunner(stream=fp,title="百度搜索测试报告",description="运行环境：Window 10,Chrome 浏览器")
    runner.run(suits)
    fp.close()
    send_mail(html_report)