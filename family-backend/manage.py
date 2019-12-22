# encoding:utf-8
# !/usr/bin/env python

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from main import create_app

app = create_app()
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@app.route('/delete',methods = ['GET','POST'])
def delete_ok():
    print('1111')
    return 'delete ok'

if __name__ == '__main__':
    print("1234")
    app.run(host='127.0.0.1', port=5000, debug=True)
    #manager.run()