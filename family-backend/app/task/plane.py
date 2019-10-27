# encoding:utf-8
# !/usr/bin/env python

from flask import Blueprint
from app.task.subtask import air_tickets

plane = Blueprint('plane',__name__)

@plane.route('/searchAirtickets',methods = ['GET','POST'])
def searchAirtickets():
    print('search plane tickets...')
    subtask = air_tickets.apply_async(args=['wuxing'], queue='que_wxx')
    return 'start search plane tickets'