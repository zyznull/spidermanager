# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import json
import requests
import re
import random

#微信公众号账号
user="362243277@qq.com"
#公众号密码
password="ZYZ960620"
#设置要爬取的公众号列表
gzlist=['What']

#登录微信公众号，获取登录之后的cookies信息，并保存到本地文本中
def weChat_login():
    #定义一个空的字典，存放cookies内容
    post={}

    #用webdriver启动谷歌浏览器
    print("启动浏览器，打开微信公众号登录界面")
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    #打开微信公众号登录页面
    driver.get('https://mp.weixin.qq.com/')
    #等待5秒钟
    time.sleep(5)
    print("正在输入微信公众号登录账号和密码......")
    #清空账号框中的内容
    driver.find_element_by_xpath("./*//input[@name='account']").clear()
    #自动填入登录用户名
    driver.find_element_by_xpath("./*//input[@name='account']").send_keys(user)
    #清空密码框中的内容
    driver.find_element_by_xpath("./*//input[@name='password']").clear()
    #自动填入登录密码
    driver.find_element_by_xpath("./*//input[@name='password']").send_keys(password)

    # 在自动输完密码之后需要手动点一下记住我
    print("请在登录界面点击:记住账号")
    time.sleep(10)
    #自动点击登录按钮进行登录
    driver.find_element_by_xpath("./*//a[@class='btn_login']").click()
    # 拿手机扫二维码！
    print("请拿手机扫码二维码登录公众号")
    time.sleep(20)
    print("登录成功")
    #重新载入公众号登录页，登录之后会显示公众号后台首页，从这个返回内容中获取cookies信息
    driver.get('https://mp.weixin.qq.com/')
    #获取cookies
    cookie_items = driver.get_cookies()

    #获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
    for cookie_item in cookie_items:
        post[cookie_item['name']] = cookie_item['value']
    cookie_str = json.dumps(post)
    with open('cookie.txt', 'w+', encoding='utf-8') as f:
        f.write(cookie_str)
    print("cookies信息已保存到本地")
