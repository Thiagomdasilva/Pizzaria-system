import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


MYSQL_USER = os.getenv(
    "MYSQL_USER",
    "root"
)

MYSQL_PASSWORD = os.getenv(
    "MYSQL_ROOT_PASSWORD",
    "root"
)

MYSQL_HOST = os.getenv(
    "MYSQL_HOST",
    "localhost"
)

MYSQL_PORT = os.getenv(
    "MYSQL_PORT",
    "3306"
)

MYSQL_DATABASE = os.getenv(
    "MYSQL_DATABASE",
    "pizzaria"
)


DATABASE_URL = (
    f"mysql+pymysql://"
    f"{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}"
    f"/{MYSQL_DATABASE}"
)

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)