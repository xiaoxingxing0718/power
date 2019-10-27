# encoding:utf-8
# !/usr/bin/env python

from main import celery
from selenium import webdriver
import time

@celery.task()
def air_tickets(name):
    print('start air_tickets...')
    chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver)
    time.sleep(1)
    driver.get('https://www.baidu.com')
    driver.page_source
    print(name)
    return 'air_tickets'