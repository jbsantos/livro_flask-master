import os
import random, string

class Config(object):
    CSRF_ENABLED = True
    SECRET = 'ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://b6c6eeb1000cde:3897b760@us-cdbr-east-06.cleardb.net/heroku_4722f6254911c8e?reconnect=true:3306/livro_flask'
    SENDGRID_API_KEY = 'API_KEY'

class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True
    IP_HOST = 'us-cdbr-east-06.cleardb.net/heroku_4722f6254911c8e?reconnect=true'
    PORT_HOST = 8001
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'us-cdbr-east-06.cleardb.net/heroku_4722f6254911c8e?reconnect=true' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class ProductionConfig(Config):
    DEBUG = True
    TESTING = True
    IP_HOST = 'us-cdbr-east-06.cleardb.net/heroku_4722f6254911c8e?reconnect=true' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
     
    URL_MAIN = 'http://%s:%s/' % (IP_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

#app_active = os.getenv('FLASK_ENV')
app_active = 'production'
