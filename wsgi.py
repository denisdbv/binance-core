from flask import Flask

import os
from os import environ, path

application = Flask(__name__)

@application.route('/')
def main():
    return 'Hello'
    # return 'RDS_HOSTNAME={} RDS_PORT={} RDS_DB_NAME={} RDS_USERNAME={} RDS_PASSWORD={}'.format(os.getenv('RDS_HOSTNAME'), os.getenv('RDS_PORT'), os.getenv('RDS_DB_NAME'), os.getenv('RDS_USERNAME'), os.getenv('RDS_PASSWORD'))