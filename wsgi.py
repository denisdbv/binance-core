from flask import Flask

application = Flask(__name__)

@application.route('/')
def main():
    return 'Hello my first flaskk app at AWS BeanStalk!'