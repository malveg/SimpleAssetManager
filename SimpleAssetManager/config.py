import os

DB_PATH = os.path.join(os.path.dirname(__file__),'data', 'SimpleAssetManDB.sqlite3')
class Config:
    SECRET_KEY = 'secret'  # change it
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))



class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DB_PATH


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DB_PATH


class ProductionConfig(Config):
    pass


config_dict = {
    'DEVELOPMENT': DevelopmentConfig,
    'PRODUCTION': ProductionConfig,
    'TESTING': TestingConfig,

    'default': DevelopmentConfig
}
