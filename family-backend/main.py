# encoding:utf-8
# !/usr/bin/env python

from flask import Flask
from celery import Celery
from flask_cors import CORS
from config import Config

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, backend=Config.CELERY_RESULT_BACKEND)

def create_app():
    app = Flask(__name__)
    print('flask应用已启动')
    app.config.from_object(Config)
    celery.conf.update(app.config)
    CORS(app, supports_credentials=True, resources=r'/*')

    from app.task.plane import plane
    app.register_blueprint(plane, url_prefix="/plane")

    from app.task.work import work
    app.register_blueprint(work, url_prefix="/work")
    return app



