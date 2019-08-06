from sqlalchemy import Column, Integer, String

from match_games import db


class Role(db.Model):
    id = Column(Integer,
                primary_key=True)
    name = Column(String(250),
                  nullable=False)

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}')>"
