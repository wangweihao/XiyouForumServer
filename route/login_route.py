from flask import Blueprint
from flask import render_template
from flask import request

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@login.route('/login', methods=['POST'])
def user_login():
    print request.form['phone']
    print request.form['passwd']
    print 'login'
    return 'hello world'