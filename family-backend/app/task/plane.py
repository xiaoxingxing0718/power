# encoding:utf-8
# !/usr/bin/env python

from flask import Blueprint, request
from app.task.subtask import air_tickets

plane = Blueprint('plane',__name__)
def addDateZero(num) :
    if num < 10:
        num = '0' + num
    return num

@plane.route('/searchAirtickets',methods = ['GET','POST'])
def searchAirtickets():

    #if Request.method == 'Get'
    print('search plane tickets...')
    print(request.method)
    print(request.args.get('depCity'))
    print(request.args.get('arrCity'))
    print(request.args.get('depDate'))
    print(request.args.get('arrDate'))
    print(request.args.get('planetype'))
    d1 = request.args.get('depDate')
    depDate = d1.getFullYear() + '-' + addDateZero(d1.getMonth()) + '-' + addDateZero(d1.getDate() + 1)
    print('324')
    print(depDate)
    subtask = air_tickets.apply_async(args=['wuxing'], queue='que_wxx')
    return 'start search plane tickets'