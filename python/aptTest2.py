# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:57:26 2020

@author: lenovo
"""

import requests,time,re
import urllib,urllib3
import json
class api:
    
    def __init__(self,HOSTNAME,Authorization):
        self.HOSTNAME=HOSTNAME
        self.Authorization=Authorization
        
   

    def userApi(self,path,ContentType,params):
        url="https://"+self.HOSTNAME+"/"+path
        headers={#设置http头部信息
                 'Host':HOSTNAME,
                 'Authorization':self.Authorization,
                 'Content-Type':ContentType,
                 } 
        #json格式
        results = requests.post(url,params,headers=headers).text 
        #print(results)
        
        self.assertResult(results)
        
    def assertMsg(self,result):
        result_dic = json.loads(result)
        code=result_dic['code']
        results=result_dic['result']
        msg=result_dic['msg']
        if msg=="success":
            return True
        else:
            return False
    
    #def assertResult(self,results):
        
        
        
    
            
 
      
if __name__=='__main__':
    path='/cloud-service/api/consume/myContract'
    HOSTNAME='testapi.huxin315.com'
    Authorization='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2OTEzNzQ4NzIsInVzZXJJZCI6ImVERmxiZnRXV2dGb3RXUjYweEFjaGs3Zk1xTW1MNFhxS2xhQ3ZwQzlnUEdEV2N5TU9vcXBmVDlaSnAvamhua3dZRis4cnIrYXl3UE1iRHJFSVJVNTRQdXFqSnd0T055ZjFLRWM0YjlnQWNDSFRoL2taUURhQ2lLbFJqYUYvVHVGWXRvKzd6YTJRM3FGcjVxakhieEZ4Zk1SbHZkeWhZcWgvRmdtRFYwMUhtWT0iLCJpYXQiOjE2MDUwNjEyNzJ9.uG75en-_gnw2f53wsLMdV1ENozf_KGjUogv0mkUMXGGp8JoPv2ciUG2hPCiY2wuBzeVVMjDoXGO7X3jLvOplEN743b30KJ70hoY1IHmnZUhTmjf50lL81z9VAwEI7Y57HN_wL5C1RAy_fOOkcbbhQoH1vQyyxTt2hGeuszmn119skiKGWtlanqD4uLrITa96Zb0Nekp6x4aDgoPQAocDBgQewoGJb2SUY-2oOMCKIAxO7JTLbWnTv86W4_uSW3UBwt2Xw3vTcABzcrf9bLesAEaLslununszfZ5XwO_9XyFga49wigKjUfj2ZuprKtfxSfI9Udp7yVlAOJttXhu50g'
    ContentType="application/x-www-form-urlencoded"
    params = {'pageNum':1,"showAll":"false"}
    api=api(HOSTNAME,Authorization)
    api.userApi(path,ContentType,params)
    
    