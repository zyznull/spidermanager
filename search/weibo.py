from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import re
import json
import time


def login():
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver') #这个是chormedriver的地址
    driver.get('https://m.weibo.cn/')
    driver.find_element_by_link_text('登录').click()
    sleep(5)
    driver.find_element_by_id('loginName').send_keys('93zyz1996@163.com')
    driver.find_element_by_id('loginPassword').send_keys('ZYZweibo')
    driver.find_element_by_id('loginAction').click()
    sleep(20)
    cookies = driver.get_cookies()
    jsonCookies = json.dumps(cookies)
    with open('cookies.json','w') as f:
        f.write(jsonCookies)
    driver.quit()

def search(name):
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    with open('D:\code\python\Spidermanager\search\cookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    driver.get('https://m.weibo.cn/')
    for cookie in listCookies:
        driver.add_cookie(cookie)
    driver.get('https://m.weibo.cn/searchs')
    driver.find_element_by_link_text('用户').click()
    driver.find_element_by_name('queryVal').send_keys(name)
    driver.find_element_by_class_name('btn-txt').click()
    sleep(5)
    linkname = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div/h3/span').text
    if(linkname != name):
        return ''
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div/h3/span').click()
    sleep(10)
    link = driver.current_url
    linkname = re.split(r'[/&?]',link)[4]
    link = 'https://m.weibo.cn/u/'+linkname
    return link
