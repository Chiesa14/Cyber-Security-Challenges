import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
	SECRET_KEY = os.urandom(50).hex()
	MONGO_URI = os.getenv("mongodb://127.0.0.1:27017")
	DB_NAME = "candyvault"


class ProductionConfig(Config):
	pass


class DevelopmentConfig(Config):
	DEBUG = False


class TestingConfig(Config):
	TESTING = False