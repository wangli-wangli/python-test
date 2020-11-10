# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:49:24 2020

@author: lenovo
"""

class Calculator:
    """用于完成两个数的加、减、乘、除"""
    
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
        
    #加法
    def add(self):
        return self.a+self.b
    
    #减法
    def sub(self):
        return self.a-self.b
    
    #乘法
    def mul(self):
        return self.a*self.b
    
    #除法
    def div(self):
        return self.a/self.b
