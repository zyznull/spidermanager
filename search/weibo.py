from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import re
import json
import time
from pyvirtualdisplay import Display


def login():
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Firefox()
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
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Firefox()
    driver.get('https://m.weibo.cn/')
    sleep(2)
    with open('./cookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        driver.add_cookie(cookie)
    driver.get('https://m.weibo.cn/searchs')
    sleep(5)
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
    driver.quit()
    display.stop()
    return link

if __name__ == '__main__':
    print(search('JY戴士'))
