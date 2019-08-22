from marshmallow import EXCLUDE, fields, validate

from match_games import ma


class CreateGameStoreSerializer(ma.Schema):
    game_id = fields.Integer(required=True,
                             error_messages={'required': 'Game must be informed.'})
    store_id = fields.Integer(required=True,
                              error_messages={'required': 'Store must be informed.'})
    value = fields.Float(required=True,
                         error_messages={'required': 'Value must be informed.'})


create_game_store_serializer = CreateGameStoreSerializer(unknown=EXCLUDE)
