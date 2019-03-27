from os import getenv

class Config:
    APP_PORT = int(getenv('APP_PORT', 4000))
    DEBUG = eval(getenv('DEBUG', "0"))

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    MONGODB_HOST = getenv('MONGODB_URI')

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    MONGODB_HOST = getenv('MONGODB_URI_TEST')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}