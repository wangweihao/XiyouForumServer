# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/21

from server import db
from mysql_modal import User
from mysql_modal import UserInfo
from mysql_modal import UserAchieve

def insert_user(account, passwd, name):
    user = User(account=account, passwd=passwd, name=name)
    from server import app
    db.session.add(user)
    db.session.flush()
    user_info = _insert_user_info(user.id)
    user_achieve = _insert_user_achieve(user.id)
    db.session.commit()
    return user

def _insert_user_info(user_id):
    user_info = UserInfo(user_id=user_id)
    db.session.add(user_info)
    return user_info

def _insert_user_achieve(user_id):
    user_achieve = UserAchieve(user_id=user_id)
    db.session.add(user_achieve)
    return user_achieve