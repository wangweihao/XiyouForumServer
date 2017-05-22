# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/22

import json
import random

import top.api
from config import AUTH_NUM_CONF

def gen_auth_number(phone_number):
    random_num = str(random.randint(100000, 999999))
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(AUTH_NUM_CONF['app_key'],
                                 AUTH_NUM_CONF['app_secret']))
    req.extend = ''
    req.sms_type = AUTH_NUM_CONF['type']
    req.sms_free_sign_name = AUTH_NUM_CONF['sign_name']
    req.sms_param = json.dumps({
        'captcha_code': random_num
    })
    req.rec_num = phone_number
    req.sms_template_code = AUTH_NUM_CONF['sms_template_code']
    try:
        resp = req.getResponse()['alibaba_aliqin_fc_sms_num_send_response']
        return resp['result']['success'], random_num
    except Exception, e:
        print e