from dotenv import load_dotenv
load_dotenv()
import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLASK_ENV= 'development'
    TESTING = False
    DEBUG = False

    SECRET_KEY = os.getenv('SECRET_KEY', default= 'A bad secret key')

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', default= 'sqliite:///{os.path.join(basedir, "instance", "app.db")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', default= 'sqliite:///{os.path.join(basedir, "instance", "test.db")}')

class ProductionConfig(Config):
    FLASK_ENV = 'production'

