# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 00:55:18 2020

@author: lenovo
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮件主题
subject='Python email test'
#授权码：HGDFAIMHMWDKQYWJ
#编写HTML类型的邮件正文
msg=MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject']=Header(subject,'utf-8')
 
#发送邮件
msg['from'] = 'wl15176128570@126.com'
msg['to'] = '15176128570@139.com'
smtp=smtplib.SMTP()
smtp.connect("smtp.126.com")
smtp.login("wl15176128570@126.com","HGDFAIMHMWDKQYWJ")
smtp.sendmail("wl15176128570@126.com","15176128570@139.com",msg.as_string())
smtp.quit()