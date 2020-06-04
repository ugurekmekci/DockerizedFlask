# config.py


import os

class BaseConfig(object):
     SECRET_KEY = 'hi'
     DEBUG = True
     DB_NAME = 'postgres'
     DB_SERVICE = '0.0.0.0'
     DB_PORT = 5432
     SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres:5432/postgres'
