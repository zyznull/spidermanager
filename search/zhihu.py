from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import re
import json
import time


def search(name):
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver') #这个是chormedriver的地址
    driver.get('https://www.zhihu.com/explore')
    name = name
    driver.find_element_by_id('q').send_keys(name)
    driver.find_element_by_class_name('zu-top-search-button').click()
    sleep(10)
    #driver.find_element_by_xpath('//h2[@class = "ContentItem-title"]/div/h2[@class = "ContentItem-title"]').click()
    linkname = driver.find_element_by_class_name('Highlight').text
    url = driver.find_element_by_class_name('ColumnLink').get_attribute('href')
    driver.quit()
    if name == linkname:
        return url
    return ''
