from os.path import dirname, join

ROOT_DIR = dirname(__file__)

UPLOAD_DIR = join(ROOT_DIR, 'static', 'uploads')


class Config:
    SECRET_KEY = '716030d5aff7e2140d6f1f52847ab80ffc93559d06708c449f834d04ff54cb4a'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROOT_DIR = ROOT_DIR
    UPLOAD_DIR = UPLOAD_DIR


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:postgres@localhost/match_games'
