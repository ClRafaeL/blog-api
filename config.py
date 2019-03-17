from os import getenv

class Config:
    APP_PORT = int(getenv('APP_PORT', 4000))
    DEBUG = eval(getenv('DEBUG', "0"))

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}