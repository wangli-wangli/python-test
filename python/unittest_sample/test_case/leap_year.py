# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:02:49 2020

@author: lenovo
"""
class LeapYear:
    """计算某年是闰年"""
    
    def __init__(self,year):
        self.year=int(year)
        
    def answer(self):
        year=self.year
        if year%100==0:
            if year%400==0:
                #整百年能被400整除的是闰年
                return "{0}是闰年".format(year)
            else:
                return "{0}不是闰年".format(year)
        else:
            if year%4==0:
                #非整年能被4整除的是闰年
                return "{0}是闰年".format(year)
            else:
                return "{0}不是闰年".format(year)
