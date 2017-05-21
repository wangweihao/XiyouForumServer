from flask import Flask
from route.login_route import login
from route.captcha_route import captcha
from route.home import home

app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(captcha)
app.register_blueprint(home)


if __name__ == '__main__':
    app.run(port=9090)