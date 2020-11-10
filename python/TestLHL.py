# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:49:38 2020

@author: lenovo
"""

#引入unittest
import unittest
#引入报告模板
import HTMLTestRunner
#引入request库
import requests
#引入json管理
import json
 
#测试类，继承了unittest.TestCase
class TestLHL(unittest.TestCase):
    #用于初始化操作可选
    def setUp(self):
        #地址前缀
        self.base_url='http://v.juhe.cn'
        #设置请求头信息
        self.headers={'Content-Type':'application/json'}
    #用于结束之后的清理工作，可选
    def tearDown(self):
        pass
    
    #@unittest.skip("这句如果注释掉就会跳过此用例不执行")
    #测试case,一定是以test开头
    def test_LHL_1(self):
        '''date格式正确'''
        #完整的接口请求地址
        self.full_url=self.base_url+'/laohuangli/d'
        #接口请求参数
        self.params={'key':'key','date':'2018-01-01'}
        #异常处理模块
        try:
            #调用requests库中的get方法请求接口
            r=requests.get(self.full_url,params=self.params,headers=self.headers)
            #对返回的内容进行解码
            json_r=r.json()
            #打印相关内容
            print('HTTP状态码=',r.status_code)
            print('响应时间（毫秒)=',r.elapsed.microseconds)
            #断言检查，返回的error_code是否为0
            self.assertEqual(json_r['error_code'],0)
            print("实际结果符合预期结果")
            print("响应内容=",json_r)
        except Exception as e:
            print('错误：%s'%e)
#通过添加类名来运行
all_suite=unittest.makeSuite(TestLHL)
#设置为调试模式，可以看到更多日志输出
runner=unittest.TextTestRunner(verbosity=2)
#设置报告保存位置F:\python
filename='F://python/report.html'
#以写方式打开，准备写入数据
fp=open(filename,'wb')
#执行测试，并写入数据
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='接口测试报告',description='接口测试')
runner.run(all_suite)
#关闭文件，如果不关闭则无法写入数据
fp.close()
    
            