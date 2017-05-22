# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/17

import json

from flask import Blueprint
from flask import request

from service import captcha_service as reg_serv

captcha = Blueprint('captcha', __name__)

@captcha.route('/captcha', methods=['POST'])
def user_put_captcha():
    # TODO: interceptor check form argu
    form = request.form
    if reg_serv.check_captcha(form['phone'], form['captcha']) == False:
        captcha_url = reg_serv.gen_captcha(form['phone'])
        return json.dumps({
            'status': 1,
            'captcha_url': captcha_url
        })
    else:
        return json.dumps({
            'status': 0
        })

@captcha.route('/captcha', methods=['GET'])
def user_get_captcha():
    # TODO: interceptor check form argu
    phone_number = request.args['phone']
    captcha_url = reg_serv.get_captcha(phone_number)
    return json.dumps({
        'status': 0,
        'captcha_url': captcha_url
    })

