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
    jd_url = 'https://jipiao.jd.com/ticketquery/flightSearch.action?_charset_=utf-8&query.depCity=%E6%88%90%E9%83%BD&query.arrCity=%E6%9D%AD%E5%B7%9E&query.lineType=RT&query.depDate=2019-11-04&query.arrDate=2019-11-06&query.queryModule=2'
    time.sleep(1)
    driver.get(jd_url)
    driver.page_source
    print(name)
    return 'air_tickets'