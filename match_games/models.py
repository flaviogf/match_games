from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from match_games import db


class Role(db.Model):
    id = Column(Integer,
                primary_key=True)
    name = Column(String(250),
                  nullable=False)
    users = relationship('User', backref='role')

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}')>"


class User(db.Model):
    id = Column(Integer,
                primary_key=True)
    name = Column(String(250),
                  nullable=False)
    email = Column(String(250),
                   nullable=False,
                   unique=True)
    password = Column(String(250),
                      nullable=False)
    image = Column(String(250),
                   nullable=False)
    role_id = Column(Integer,
                     ForeignKey('role.id'),
                     nullable=False)

    def __repr__(self):
        return f"<User(id=None, name='{self.name}', role='{self.role.name}')>"
