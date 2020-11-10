# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 00:05:45 2020

@author: lenovo
"""

import pytest

#设置钩子
@pytest.fixture()
def test_url():
    return "http://www.baidu.com"

def test_baidu(test_url):
    print(test_url)