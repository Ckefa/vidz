import os

MYSQL_HOST = os.getenv("MYSQL_HOST").strip()
MYSQL_USER = os.getenv("MYSQL_USER").strip()
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD").strip()
MYSQL_DB = os.getenv("MYSQL_DB").strip()


class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{
        MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
