# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:14:13 2020

@author: wangli
"""
import requests,time,re
import urllib,urllib3
HOSTNAME='https://api.jyfwyun.com/search-service/cross/labelSearch'

#取用户登录的token值
def GetToken():
    global token   #定义token为全局变量
    url='http://'+HOSTNAME+'/buyer/user/login.do'
    params={   #参数为登录手机号和密码                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        'phone':'11111111',
        'pwd':'1232234342'
        }
    request=urllib3.Request(url=url,data=urllib.urlencode(params))#发送接口请求url和参数
    response=urllib3.urlopen(request)#返回响应数据
    data=response.read()#返回响应数据
    regx='.*"token":"(.*)","ud"'#正则表达式token,左匹配"token":",右匹配","ud"'
    pm=re.search(regx, data)#取token匹配值
    token=pm.group(1)#如果匹配到返回token值
    regy=r'"state":(\d+)}'#正则表达式state,左匹配"state":,右匹配}
    pn=re.search(regy,data)#如果匹配到则返回token值
    state=pn.group(1)#匹配到state值
    if state=='0':
        return True#登录成功
    return False#登录失败

    
    
    

#读取1个接口用例
def interfaceTest(case_list):
    
    res_flags=[]
    request_urls=[]
    responses=[]
    for case in case_list:
        try:
            case_id=case[0]#用例id
            interface_name=case[1]#接口名称
            method=case[3]#接口方法
            url=case[5]#接口url地址
            param=case[2]#接口参数
            res_check=case[4]#接口返回值校验
        except Exception:
            return '测试用例格式不正确！'
        if param=='':
            new_url='http://'+HOSTNAME+url #接口参数为空，接口为HOSTNAME+url
        elif param=='null':
            new_url='http://'+HOSTNAME+url #接口参数为null，接口为HOSTNAME+url
        else:
            new_url='http://'+HOSTNAME+url+'?'+urlparam(param) #如果接口有参数，接口为HOSTNAME+url+param
        if method.upper()=='GET':#如果为get方法
            print(str(case_id)+''+new_url)
            headers={#设置http头部信息
                     'Host':HOSTNAME,
                     'Connnect':'keep-alive',
                     'token':token,
                     'Content-Type':'application/x-www-form-urlencoded',
                     'User-Agent':'Apache-HttpClient/4.2.6(java1.5)'} 
            data=None
            results = requests.get(new_url,data,headers=headers).text #发送get请求，results得到请求的返回数据
            responses.append(results)
            res=readRes(results,res_check)#对请求的返回数据进行校验，校验结果有三种：pass,fail,jFIF
        
            if 'pass'==res: #测试用例通过
                writeResult(case_id,'pass')
                res_flags.append('pass')
                if JFIF(results):#校验JFIF为图片
                    results='JFIF ok'
                else:
                    print(u'接口名称：'+interface_name)
                    print(u'接口地址：'+new_url)
                    print(u'响应数据：'+results)
                
                    print(str(case_id)+'-----------'+'success'+'----------')
                    continue
            else:  #测试用例失败
                res_flags.append('fail')
                writeResult(case_id,'fail')
                if reserror(results):#接口返回数据错误
                    writeBug(case_id,interface_name,new_url,"api response is error",res_check)
                else:#校验数据错误
                    writeBug(case_id,interface_name,new_url,results,res_check)
                print(u'接口名称：'+interface_name)
                print(u'接口地址：'+new_url)
                print(u'响应数据：'+results)
                
                print(str(case_id)+'-----------'+'fail'+'----------')
        else:#如果为post方法
            print(str(case_id)+''+new_url)
            headers={#设置http头部信息
                     'Host':HOSTNAME,
                     'Connnect':'keep-alive',
                     'token':token,
                     'Content-Type':'application/x-www-form-urlencoded',
                     'User-Agent':'Apache-HttpClient/4.2.6(java1.5)'} 
            data=None
            results = requests.post(new_url,data,headers=headers).text #发送get请求，results得到请求的返回数据
            responses.append(results)
            res=readRes(results,res_check)#对请求的返回数据进行校验，校验结果有三种：pass,fail,jFIF
        
            if 'pass'==res: #测试用例通过
                writeResult(case_id,'pass')
                res_flags.append('pass')
                if JFIF(results):#校验JFIF为图片
                    results='JFIF ok'
                else:
                    print(u'接口名称：'+interface_name)
                    print(u'接口地址：'+new_url)
                    print(u'响应数据：'+results)
                
                    print(str(case_id)+'-----------'+'success'+'----------')
                    continue
            else:  #测试用例失败
                res_flags.append('fail')
                writeResult(case_id,'fail')
                if reserror(results):#接口返回数据错误
                    writeBug(case_id,interface_name,new_url,"api response is error",res_check)
                else:#校验数据错误
                    writeBug(case_id,interface_name,new_url,results,res_check)
                print(u'接口名称：'+interface_name)
                print(u'接口地址：'+new_url)
                print(u'响应数据：'+results)
                
                print(str(case_id)+'-----------'+'fail'+'----------')
              
                
            
            
def writeBug(bug_id,interface_name,request,response,res_check):
    interface_name=interface_name.encode('utf-8')#写测试bug
    res_check=res_check.encode('utf-8')#校验字段
    response=response.encode('utf-8')
    request=request.encode('utf-8')
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    bug_title=str(bug_id)+'_'+interface_name+'_出错了'
    step='[请求报文]'+request+'<br/>'+'[预期结果]'+res_check+'<br/>'+'[响应报文]'+response
               
                
        
 #校验结果，如一致则返回pass,否则返回错误提示
def readRes(res,res_check):
     res=res.replace('":"',"=").replace('":',"=")#校验时替换符号为=号，再进行校验
     res_check=res_check.split(';')
     for s in res_check:
         if s in res:
             pass
         else:
             return u'错误，返回参数和预期结果不一致'+str(s)
     return 'pass'
    
def writeResult(case_id,result):
    result=result.encode('utf-8')
    print(case_id,result)
      
            
         


def urlparam(param):
    #参数值的替换
    param1=param.replace('*','&')#如果参数再数据库中为*，则替换成&
    param2=param1.replace('&quto;','\"')#如果参数再数据库中为&quto;,则替换成"
    return param2.replace(';','&')#如果参数再数据库中为；，则替换成&

#判断返回图片是否正确
def JFIF(results):
    global JFIF
    regx='JFIF'
    pm=re.search(regx,results)
    if pm:
        return regx
    return False

def reserror(results):#regx变量赋值为html字符串，如果服务器异常时会返回4040等html标志，进行匹配
    global html
    regx='html'
    
    pm=re.search(regx, results)
    if pm:
        return regx
    return False

            
                 

    