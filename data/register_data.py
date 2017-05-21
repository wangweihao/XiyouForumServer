# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/21

from db.mysql_db import db
from db.mysql_modal import User
from db.mysql_modal import UserInfo
from db.mysql_modal import UserAchieve

def insert_user(account, passwd, name):
    user = User(account=account, passwd=passwd, name=name)
    db.session.add(user)

def insert_user_info():
    user_info = UserInfo()
    db.session.add(user_info)

