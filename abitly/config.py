from dotenv import load_dotenv

# Exports all the ENV Variables of the .env file
load_dotenv()


class Config:
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
