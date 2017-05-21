# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/22

from flask import Blueprint

register = Blueprint('register', __name__)

@register.route('/register', methods=['POST'])
def user_register():
    pass