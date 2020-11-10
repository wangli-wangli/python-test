# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:46:51 2020

@author: lenovo
"""

import pytest

if __name__=='__main__':
    #pytest.main(['-s','./test_dir'])
    #生成JUnit XML文件
    #pytest.main(['./test_dir','--junit-xml=./report/log.xml'])
    #生成在线报告
    #pytest.main(['./test_dir','--pastebin=all'])
    
    #pytest.main(['-s','-v','test_project\\'])
    
    pytest.main(['./--html=./report/result.html'])