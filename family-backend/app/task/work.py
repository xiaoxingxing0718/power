# encoding:utf-8
# !/usr/bin/env python

from flask import Blueprint, request
from app.task.subtask import air_tickets

work = Blueprint('work',__name__)

@work.route('/workregister',methods = ['GET','POST'])
def workregister():
    if request.method == 'POST':
        print('start....')
        weixin = request.form.get('weixin')
        phone = request.form.get('phone')
        taobao = request.form.get('taobao')
        location = request.form.get('location')

        print('search weixin...', weixin)
        print('search phone...', phone)
        print('search taobao...', taobao)
        print('search location...', location)

    return 'start compute...'