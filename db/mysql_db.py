# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/20

from flask_sqlalchemy import SQLAlchemy

from server import app
from config import MYSQL_CONF

def init_mysql():
    db_uri = ''.join(['mysql+', MYSQL_CONF['connector'], '://', MYSQL_CONF['user'],
                   ':', MYSQL_CONF['passwd'], '@', MYSQL_CONF['host'], ':',
                   MYSQL_CONF['port'], '/', MYSQL_CONF['db'], '?charset=utf8'])
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app, use_native_unicode='utf-8')
    return db

db = init_mysql()
