from flask import Flask
from route.login_route import login
from route.captcha_route import captcha
from route.home_route import home
from route.register_route import register

from db.mysql_db import init_mysql

app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(captcha)
app.register_blueprint(home)
app.register_blueprint(register)

db = init_mysql(app)

if __name__ == '__main__':
    app.run(port=9090)