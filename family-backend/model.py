# encoding:utf-8
# !/usr/bin/env python

from manage import db

#db.drop_all()
db.create_all()

class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True)
    weixin = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(10), unique=True)
    taobao = db.Column(db.String(80), unique=True)
    localcation = db.Column(db.String(1024))
    distance = db.Column(db.String(256))
    checkperson = db.Column(db.String(256))
    description = db.Column(db.String(2048))
    fromwhere = db.Column(db.String(256))
    checkresult = db.Column(db.String(128))
    turn = db.Column(db.String(256))

    def __repr__(self):
        return '<User %r>' % self.weixin