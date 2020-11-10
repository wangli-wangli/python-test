# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:45:49 2020

@author: lenovo
"""

from poium import Page,PageElement

class LoginPage(Page):
    """
    登录Page类
    """
    username=PageElement(css='#loginAccount',describe="用户名")
    password=PageElement(css='#loginPwd',describe="密码")
    user_info=PageElement(css="a.nav_user_name>span",describe="用户信息")
    