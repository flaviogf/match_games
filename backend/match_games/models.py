from match_games import db
from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(250),
                     nullable=False)
    email = db.Column(db.String(250),
                      nullable=False)
    password = db.Column(db.String(250),
                         nullable=False)
    image = db.Column(db.String(250),
                      nullable=False,
                      default='default.jpg')
    role = db.Column(db.String(250),
                     nullable=False)


class Game(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(250),
                     nullable=False)
    image = db.Column(db.String(250),
                      nullable=False,
                      default='default.jpg')
    stores = relationship('GameStore', back_populates='game')


class Store(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(250),
                     nullable=False)
    image = db.Column(db.String(250),
                      nullable=False,
                      default='default.jpg')
    games = relationship('GameStore', back_populates='store')


class GameStore(db.Model):
    game_id = db.Column(db.Integer,
                        db.ForeignKey('game.id'),
                        primary_key=True)
    store_id = db.Column(db.Integer,
                         db.ForeignKey('store.id'),
                         primary_key=True)
    value = db.Column(db.Float,
                      nullable=False)
    store = relationship('Store', back_populates='games')
    game = relationship('Game', back_populates='stores')
