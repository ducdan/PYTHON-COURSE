import os
# default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    SECRET_KEY = 'this is secret key'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:thanhsg7@localhost:5432/Ex1'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:thanhsg7@localhost:5432/Ex1'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False