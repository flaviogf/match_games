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
