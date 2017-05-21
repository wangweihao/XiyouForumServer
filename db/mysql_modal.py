# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/21

from mysql_db import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(64), unique=True, nullable=True)


db.create_all()
