# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/22

import json

from flask import Blueprint
from flask import request

from db.redis_db import rds

register = Blueprint('register', __name__)

@register.route('/register', methods=['GET'])
def user_get_register_num():
    # TODO: check register form
    phone = str(request.args['phone'])

    from utils.gen_auth_number import gen_auth_number
    ret = gen_auth_number(phone)
    if ret[0] == True:
        rds.hset(phone, 'auth_number', ret[1])
    else:
        print 'set auth error'
    return json.dumps({'status': 0})

@register.route('/register', methods=['POST'])
def user_register():
    from service.register_service import user_register
    if user_register(request.form) == True:
        print 'success'
        return json.dumps({
            'status': 0
        })
    else:
        print 'error'
        return json.dumps({
            'status':1
        })
