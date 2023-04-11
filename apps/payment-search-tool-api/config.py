"""Flask config."""

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS='Content-Type'
    TEMP_FOLDER='temp'


class ProdConfig(Config):
    """Production config"""
    FLASK_ENV = 'prod'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_SQLALCHEMY_DATABASE_URI')

class DevConfig(Config):
    """Development config"""
    FLASK_ENV = 'dev'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_SQLALCHEMY_DATABASE_URI')

class LocalConfig(Config):
    """LocalServer config"""
    FLASK_ENV = 'local'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('LOCAL_SQLALCHEMY_DATABASE_URI')
    
