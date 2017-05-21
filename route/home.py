# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/20

from flask import Blueprint
from flask import request
from flask import render_template

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def get_hom_page():
    return render_template('index.html')

