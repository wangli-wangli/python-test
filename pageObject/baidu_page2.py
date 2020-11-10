# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:31:34 2020

@author: lenovo
"""

from poium import Page,PageElement

class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    search_input=PageElement(id_="kw",timeout=5)
    search_button=PageElement(id_="su",timeout=30)
    