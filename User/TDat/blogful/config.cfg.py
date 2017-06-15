

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:123456@localhost:5432/blogful'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:123456@localhost:5432/blogful'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False