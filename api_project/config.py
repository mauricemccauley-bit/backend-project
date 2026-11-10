import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("JWT_SECRET")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///dev.db")


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}