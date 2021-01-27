# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 00:55:18 2020

@author: lenovo
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

#发送邮件主题
subject='Python email test'

#发送的附件
with open('log.txt','rb') as f:
    send_att=f.read()
    
    

#授权码：HGDFAIMHMWDKQYWJ
#编写HTML类型的邮件正文
att=MIMEText(send_att,'text','utf-8')
att["Content-Type"]="application/octet-stream"
att["Content-Disposition"]='"attachment;filename="log.txt"'

msg=MIMEMultipart()
msg["Subject"]=subject
msg.attach(att)
#登录密码：2024410102
#发送邮件
msg['from'] = 'wl15176128570@126.com'
msg['to'] = '15176128570@139.com'
smtp=smtplib.SMTP()
smtp.connect("smtp.126.com")
smtp.login("wl15176128570@126.com","HGDFAIMHMWDKQYWJ")
smtp.sendmail("wl15176128570@126.com","15176128570@139.com",msg.as_string())
smtp.quit()