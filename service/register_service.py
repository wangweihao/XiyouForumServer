# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/22

import hashlib
import traceback

from db.redis_db import rds
from db.user_tb import insert_user


def user_register(form):
    if form['auth_number'] == rds.hget(form['phone'], 'auth_number'):
        m = hashlib.md5()
        m.update(form['passwd'])
        passwd = m.hexdigest()
        user = insert_user(form['phone'], passwd, form['name'])
        return True
    else:
        return False
