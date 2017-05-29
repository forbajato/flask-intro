import os

# default config
# Be sure to set an environment variable (called DATABASE_URL) pointing
# to the database.


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "my precious"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
