# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:39:23 2020

@author: lenovo
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep,ctime
import time
from selenium.webdriver.support.select import Select
import os

def setWindowSize():
    driver=webdriver.Chrome()
    driver.get("http://m.baidu.com")
    
    #参数数字为像素
    print("设置浏览器宽480、高800显示")
    driver.set_window_size(480,800)
    driver.quit()

def backAndForward():
    driver=webdriver.Chrome()
    #访问百度首页
    first_url='http://www.baidu.com'
    print("now access %s"%(first_url))
    driver.get(first_url)
    
    #访问新闻页
    second_url='http://news.baidu.com'
    print("now access %s"%(second_url))
    driver.get(second_url)
    
    #返回到百度首页
    print("back to %s"%(first_url))
    driver.back()
    
    #前进到新闻页
    print("forward to %s"%(second_url))
    driver.forward()
    
    #浏览器刷新
    driver.refresh()
    
    driver.quit()
    
#操作元素
def doElement():
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")
    #清除文本
    driver.find_element_by_id("kw").clear()
    #模拟按键输入
    driver.find_element_by_id("kw").send_keys("selenium")
    #单击元素
    driver.find_element_by_id("su").click()    
    
    driver.quit()

#提交表单
def submit():
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")
    
    search_text=driver.find_element_by_id("kw")
    search_text.send_keys('selenium')
    search_text.submit()
    
    driver.quit()
    
#其他操作
def others():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")

    #获得输入框的尺寸
    size=driver.find_element_by_id("kw").size
    print(size)
    
    #返回百度页面底部备案信息
    text=driver.find_element_by_id("bottom_layer").text
    print(text)
    
    #返回元素的属性值，可以是id,name,type或其他任意属性
    attribute=driver.find_element_by_id("kw").get_attribute("type")
    print(attribute)
    
    #返回元素的结果是否可见，返回结果是True或False
    result=driver.find_element_by_id("kw").is_displayed()
    print(result)

    driver.quit()
    
#鼠标悬浮操作方法
def mouseAction():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    #定位到要悬浮的元素
    above=driver.find_element_by_id("s-usersetting-top")
    #对定位到的元素执行鼠标悬停操作
    ActionChains(driver).move_to_element(above).perform()
    
def keyboardAction():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    #再输入框输入内容
    driver.find_element_by_id("kw").send_keys("selenium")
    
    #删除多输入的一个m
    driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
    
    #输入空格键+“教程”
    driver.find_element_by_id("kw").send_keys(Keys.SPACE)
    driver.find_element_by_id("kw").send_keys("教程")

    #输入组合键Ctrl+a,全选输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
    
    #用回车键代替单机操作
    driver.find_element_by_id("su").send_keys(Keys.ENTER)
    
    driver.quit()

#获得验证信息
def getInformation():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    print("Before search==================")
    
    #打印当前页面的title
    title=driver.title
    print("title:"+title)
    
    #打印当前页面的url
    now_url=driver.current_url
    print("URL:"+now_url)
    
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()

    print("After search==================")
    
     #再次打印当前页面的title
    title=driver.title
    print("title:"+title)
    
    #再次打印当前页面的url
    now_url=driver.current_url
    print("URL:"+now_url)
    
    #获取搜索结果条数
    num=driver.find_element_by_class_name('nums').text
    print("result:"+num)
    
    driver.quit()
    
#显式等待
def wait1():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    #判断元素是否存在
    element=WebDriverWait(driver,5,0.5).until(EC.visibility_of_all_elements_located(By.ID,"kw"))
    element.send_keys('selenium')
    driver.quit()  

#显示等待
def wait2():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    print(ctime)
    for i in range(10):
        try:
            el=driver.find_element_by_id("kw22")
            if el.is_displayed():
                break
        except:
            pass
        sleep(1)
    else:
        print("time out")
    print(ctime())
    
    driver.quit()
    
#隐式等待
def wait3():
    driver=webdriver.Chrome()
    
    #设置隐式等待10s
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    
    try:
        print(ctime())
        driver.find_element_by_id("kw22").send_keys('selenium')
    except NoSuchElementException as e:
        print(e)
    finally:
        print(ctime())
        driver.quit()
        
#定位一组元素
def findElements():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep()
    
    #定位一组元素
    texts=driver.find_element_by_xpath("//div[@tpl='se_com_default']/h3/a")
    
    #计算匹配结果个数
    print(len(texts))
    
    #循环遍历出每一条搜索结果的标题
    for t in texts:
        print(t.text)

    driver.quit()  

#切换表单
def switchFrame():
    driver=webdriver.Chrome()
    driver.get("http://www.126.com")
    sleep(2)
    
    login_frame=driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
    driver.switch_to.frame(login_frame)
    driver.find_element_by_name("email").send_keys("username")
    driver.find_element_by_id("password").send_keys(("password"))
    driver.find_element_by_id("dologin").click()
    driver.switch_to.default_content()

    driver.quit() 
    
#切换窗口
def switchWindow():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    
    #获得百度搜索窗口句柄
    search_windows=driver.current_window_handle
    
    driver.find_element_by_link_text('登录').click()
    driver.find_element_by_link_text("立即注册").click()
    
    #获得当前所有打开的窗口句柄
    all_handles=driver.window_handles
    
    #进入注册窗口
    for handle in all_handles:
        if handle!=search_windows:
            driver.switch_to.window(handle)
            print(driver.title)
            driver.find_element_by_name("userName").send_keys('username')
            driver.find_element_by_name('phone').send_keys('15176128570')
            time.sleep(2)
            #关闭当前窗口
            driver.close()
            
    #回到搜索窗口
    driver.switch_to.window(search_windows)
    print(driver.title)
    
    driver.quit()
    
#警告框处理
def doAlert():
    driver=webdriver.Chrome()
    driver.get('https.//www.baidu.com')
    
    #打开搜索设置
    link=driver.find_element_by_link_text('设置').click()
    driver.find_element_by_link_text("搜索设置").click()
    
    #保存设置
    driver.find_element_by_class_name("prefpanelgo").click()
    
    #获取警告框
    alert=driver.switch_to.alert
    
    #获取警告框提示信息
    alert_text=alert.text
    print(alert_text)
    
    #接取警告框
    alert.accept()
    
    driver.quit()
    
#下拉框处理
def doSelect():
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    
    #打开搜索设置
    link=driver.find_element_by_link_text('设置').click()
    driver.find_element_by_link_text("搜索设置").click()
    sleep(2)
    
    #搜索结果显示条数
    sel=driver.find_element_by_xpath("//select[@id='nr']")
    
    #value="20"
    Select(sel).select_by_value('20')
    sleep(2)

    #<option>每页显示50条</option>
    Select(sel).select_by_visible_text("每页显示50条")
    sleep(2)
    
    #根据下拉框选项的索引进行选择
    Select(sel).select_by_value(0)
    sleep(2)
    
    driver.quit()

#上传文件
def uploadFile():
    file_path=os.path.abspath('./files')
    driver=webdriver.Chrome()
    upload_page='file:///'+file_path+'upfile.html'
    driver.get(upload_page)

    #定位上传按钮，添加本地文件
    driver.find_element_by_id("file").send_keys(file_path+'test.txt')
    
#下载文件
def downloadFile():
    options=webdriver.ChromeOptions()
    prefs={'profile.default_content_setting.popups':0,
           'download.default_directory':os.getcwd()}
    options.add_experimental_option('prefs',prefs)
    
    driver=webdriver.Chrome(chrome_options=options)
    driver.get("https://pyapi.org/project/selenium/#files")
    driver.find_element_by_link_text("selenium-3.141.0.tar.gz").click()
    
#获得cookie
def getCookie():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    #获得所有Cookie信息并打印
    cookie=driver.get_cookies()
    print(cookie)
    
#添加cookie
def setCookie():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    #添加cookie信息
    driver.add_cookie({"name":"key-aaaaaa","value":"value-bbbbbb"})
    
    #遍历指定的Cookie
    for cookie in driver.get_cookies():
        print("%s->%s"%(cookie['name'],cookie['value']))
        
#调用javascript
def callJavascript():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    driver.set_window_size(800,600)
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()

    #通过JavaScript设置浏览器窗口的滚动条位置
    js="window.scrollTo(100,450);" 
    driver.execute_script(js)
      
#处理HTML5视频播放
def HTML5():
    driver=webdriver.Chrome()
    driver.get("http://videojs.com/")
    
    video=driver.find_element_by_id("preview-player_html5_api")
    
    #返回播放文件地址
    url=driver.execute_script("return arguments[0].currentSrc;",video)
    print(url)
   
    #播放视频
    print("start")
    driver.execute_script("arguments[0].play()",video)

    #播放15秒
    sleep(15)

    #暂停视频
    print("stop")
    driver.execute_script("arguments[0].pause()",video)

    driver.quit()    
    
#滑动解锁
def Unclock():
    driver=webdriver.Chrome()
    driver.get("https://www.helloweba.com/demo/2017/unclock/")
    
    #定位滑动块
    slider=driver.find_element_by_class_name("slide-to-unlock-handle")[0]
    action=ActionChains(driver)

    for index in range(200):
        try:
            action.move_by_offset(2, 0).perform()
        except UnexpectedAlertPresentException:
            break
        action.reset_actions()
        sleep(0.1)#等待停顿时间
    
    #打印警告框提示
    success_text=driver.switch_to.alert.text
    print(success_text)
    
#上下滑动选择时间
def selectTime():
    driver=webdriver.Chrome()
    driver.get("http://www.jq222.com/yanshi14976")
    sleep(2)
    driver.switch_to.frame("iframe")
    driver.find_element_by_id("appDate").click()

    #定位要滑动的年、月、日
    dwwos=driver.find_elements_by_class_name("dwwo")
    year=dwwos[0]
    month=dwwos[1]
    day=dwwos[2]
    
    action=webdriver.TouchActions(driver)
    action.scroll_from_element(year,0,5).perfomr()
    action.scroll_from_element(month,0,30).perfomr()
    action.scroll_from_element(day,0,30).perfomr()
    
#截屏
def screenShoot():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    driver.save_screenshot("./files/baidu_img.png")
    

if __name__=='__main__':
    doElement()
