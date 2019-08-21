from marshmallow import EXCLUDE, fields, validate

from match_games import ma


class CreateGameSerializer(ma.Schema):
    name = fields.String(required=True,
                         validate=[validate.Length(min=3, error='Name must be {min} characters.')],)


create_game_serializer = CreateGameSerializer(unknown=EXCLUDE)
