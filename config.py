class Config:
    SECRET_KEY = 'fdb85667f97f0febb82b0c85586f659ebd049993a5d57e6eca56cd76e128c29d'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:postgres@localhost/match_games'
