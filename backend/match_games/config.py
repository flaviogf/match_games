class Config:
    SECRET_KEY = '716030d5aff7e2140d6f1f52847ab80ffc93559d06708c449f834d04ff54cb4a'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:postgres@localhost/match_games'
