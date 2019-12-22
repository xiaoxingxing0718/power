# encoding:utf-8
# !/usr/bin/env python

from flask import Blueprint, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from manage import db


work = Blueprint('work',__name__)

@work.route('/workregister',methods = ['GET','POST'])
def workregister():
    if request.method == 'POST':
        print('start....',request.method)
        print('start1....', request.args)
        print('start....', request.form)
        weixin = request.form.get("weixin")
        phone = request.form.get('phone')
        taobao = request.form.get('taobao')
        location = request.form.get('location')

        print('search weixin...', weixin)
        print('search phone...', phone)
        print('search taobao...', taobao)
        print('search location...', location)

        from model import Register
        engine = create_engine("mysql://root:@127.0.0.1:3306/family?charset=utf8")
        Session = sessionmaker(bind=engine)
        session = Session()

    return 'start compute...'