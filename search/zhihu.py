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
    driver.get('https://www.zhihu.com/explore')
    name = name
    driver.find_element_by_id('q').send_keys(name)
    driver.find_element_by_class_name('zu-top-search-button').click()
    sleep(5)
    #driver.find_element_by_xpath('//h2[@class = "ContentItem-title"]/div/h2[@class = "ContentItem-title"]').click()
    driver.find_element_by_link_text('专栏').click()
    sleep(1)
    linkname = driver.find_element_by_class_name('Highlight').text
    print(linkname)    
    url = driver.find_element_by_class_name('ColumnLink').get_attribute('href')
    driver.quit()
    display.stop()
    if name == linkname:
        return url
    return ''
if __name__ == '__main__':
	print('url' + search(u'金与火之歌'))

