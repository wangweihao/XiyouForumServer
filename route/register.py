# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/17

import json

from flask import Blueprint
from flask import request

from service import register_service as reg_serv

register = Blueprint('register', __name__)

@register.route('/register', methods=['POST'])
def user_register():
    # TODO: interceptor check form argu
    form = request.form
    if reg_serv.check_captcha(form['phone'], form['captcha']) == False:
        new_captcha_url = reg_serv.get_captcha(form['phone'])
        return json.dumps({
            'status': 0,
            'captcha': new_captcha_url
        })
    else:
        return json.dumps({
            'status': 1
        })

@register.route('/register/captcha', methods=['GET'])
def user_get_captcha():
    # TODO: interceptor check form argu
    print 'captcha'
    phone_number = request.args['phone']
    captcha_url = reg_serv.get_captcha(phone_number)
    return json.dumps({
        'captcha': captcha_url
    })

