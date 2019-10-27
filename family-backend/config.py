# encoding:utf-8
# !/usr/bin/env python

import sys
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/family?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    debug = True
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND= 'redis://localhost:6379/1'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_ENABLE_UTC = True
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'