# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/14

import config

from db.redis_db import rds
from utils import gen_captcha


expire_time = 5*60

def get_captcha(phone_number):
    streams, strs = gen_captcha.generate_verify_image(save_img=True,
                                                      img_name=phone_number)
    rds.set(phone_number, strs, ex=expire_time)
    return ''.join([config.URL_HEAD, config.URL_HOST, config.URL_CAPTCHA_PATH,
                    phone_number, config.CAPTCHA_TYPE])


def check_captcha(phone_number, captcha):
    if captcha.lower() == rds.get(phone_number).lower():
        return True
    else:
        return False

def _gen_phone_verfication():
    # TODO: generation phone verfication code
    pass