import os
# default config

class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    SECRET_KEY = 'talamaday'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:zxcvbnm1@localhost:5432/blogful'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:zxcvbnm1@localhost:5432/blogful'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
