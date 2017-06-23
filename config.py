import os

# default config
# Be sure to set an environment variable (called DATABASE_URL) pointing
# to the database.


class BaseConfig(object):
    DEBUG = False
#    SECRET_KEY = "my precious"
    SECRET_KEY = '\xf0C\x92\xf7\xa8\xf0lQ=\x85\xc1l}\x81\xa7N4\x88\xa3Y\r0\x83\x7f'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
