# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/14

import time
import json

import config

from db.redis_db import rds
from utils import gen_captcha_img


expire_time = 5*60

def get_captcha(phone_number):
    unix_timestamp = time.time()
    if (rds.exists(phone_number) == False or
            (int(rds.hget(phone_number, 'captcha_expire_time'))
                    + expire_time < int(unix_timestamp))):
        return gen_captcha(phone_number)
    else:
        return rds.hget(phone_number, 'captcha_url')

def check_captcha(phone_number, captcha):
    unix_timestamp = time.time()
    if (int(rds.hget(phone_number, 'captcha_expire_time')) + expire_time
        < int(unix_timestamp)):
        return False
    elif captcha.lower() == rds.hget(phone_number, 'captcha').lower():
        return True
    else:
        return False

def gen_captcha(phone_number):
    unix_timestamp = time.time()
    captcha_name = ''.join([str(int(unix_timestamp)), phone_number])
    streams, strs = gen_captcha_img.generate_verify_image(save_img=True,
                                                          img_name=captcha_name)
    url = ''.join([config.URL_HEAD, config.URL_HOST, config.URL_CAPTCHA_PATH,
                   captcha_name, config.CAPTCHA_TYPE])
    rds.hset(phone_number, 'captcha', strs)
    rds.hset(phone_number, 'captcha_url', url)
    rds.hset(phone_number, 'captcha_expire_time', int(time.time()))
    return url


def _gen_phone_verfication():
    # TODO: generation phone verfication code
    pass