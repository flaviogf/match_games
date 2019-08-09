from match_games import db


class Role(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(250),
                     nullable=False)
    users = db.relationship('User', backref='role')


class User(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(250),
                     nullable=False)
    email = db.Column(db.String(250),
                      nullable=False,
                      unique=True)
    password = db.Column(db.String(250),
                         nullable=False)
    image = db.Column(db.String(250),
                      nullable=False,
                      default='default.jpg')
    role_id = db.Column(db.Integer,
                        db.ForeignKey('role.id'))


game_store = db.Table('game_store',
                      db.Column('id',
                                db.Integer,
                                primary_key=True),
                      db.Column('store_id',
                                db.Integer,
                                db.ForeignKey('store.id')),
                      db.Column('game_id',
                                db.Integer,
                                db.ForeignKey('game.id')))


class Store(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(250),
                     nullable=False)
    image = db.Column(db.String(250),
                      nullable=False)


class Game(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(250),
                     nullable=False)
    image = db.Column(db.String(250),
                      nullable=False)
    stores = db.relationship('Store',
                             secondary=game_store)
