import os
# default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:12345ad@localhost:5432/Blogful'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:12345ad@localhost:5432/Blogful'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False