from marshmallow import fields, validate

from match_games import ma


class CreateGameSerializer(ma.Schema):
    name = fields.String(required=True,
                         validate=[validate.Length(min=3)])


create_game_serializer = CreateGameSerializer()