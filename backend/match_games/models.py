from match_games import db


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


class Store(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(250),
                     nullable=False)
    image = db.Column(db.String(250),
                      nullable=False,
                      default='default.jpg')


class GameStore(db.Model):
    game_id = db.Column(db.Integer,
                        db.ForeignKey('game.id'),
                        primary_key=True)
    store_id = db.Column(db.Integer,
                         db.ForeignKey('store.id'),
                         primary_key=True)
    value = db.Column(db.Float,
                      nullable=False)
