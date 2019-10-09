import os

# Postgres
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = 'db'
database = os.environ['POSTGRES_DB']
port = '5432'

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

# Redis
redis_host = os.environ['REDIS_HOST']
redis_port = os.environ['REDIS_PORT']
redis_db = os.environ['REDIS_DB']

REDIS_MESSAGE_TTL = 300  # 5 minutes
REDIS_URL = f'redis://{redis_host}:{redis_port}/{redis_db}'
