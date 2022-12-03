"""

dialect://username:password@host:port/database

# SQLite, relative to Flask instance path
sqlite:///project.db

# PostgreSQL
postgresql://scott:tiger@localhost/project

# MySQL / MariaDB
mysql://scott:tiger@localhost/project
"""
import os
from urllib.parse import quote
from redis import Redis


class BaseConfig:
    # flask-session, step two
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(host='127.0.0.1', port='6379')
    SQLALCHEMY_DATABASE_URI = f'postgresql://scott:tiger@localhost/project'

class DevConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    pass

class ProConfig(BaseConfig):
    pass


try:
    server_mode = os.environ['server_mode']
except:
    server_mode = 'dev'

if server_mode == 'dev':
    Config = DevConfig
elif server_mode == 'test':
    Config = TestConfig
elif server_mode == 'production':
    Config = ProConfig
else:
    raise Exception('ENV server_mode error, server_mode must be in (dev, test, production)')