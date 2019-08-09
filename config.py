from os import path

DIRNAME = path.dirname(__file__)

UPLOAD_FOLDER = path.join(DIRNAME,
                          'match_games',
                          'static',
                          'uploads')


class Config:
    SECRET_KEY = '0130481D1B12AC1B951B8A04F73D17B8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = UPLOAD_FOLDER


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:postgres@localhost/match_games'
