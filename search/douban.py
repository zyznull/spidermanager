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


def search(name):
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Firefox()
    driver.get('https://www.douban.com/group/search?cat=1019&q='+name)
    old_page = driver.current_url
    sleep(5)
    linkname = driver.find_element_by_xpath('//div[@class="groups"]/div/div[@class="content"]/div[@class="title"]/h3/a').text
    if linkname != name:
        return ''
    url = driver.find_element_by_xpath('//div[@class="groups"]/div/div[@class="content"]/div[@class="title"]/h3/a').get_attribute('href')
    linkname = url.split('/')[4]
    url = 'https://www.douban.com/feed/group/'+linkname+'/discussion'
    driver.quit()
    display.stop()
    return url


