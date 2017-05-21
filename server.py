from flask import Flask
from route.login import login
from route.register import register
from route.home import home

app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(home)


if __name__ == '__main__':
    app.run(port=9090)