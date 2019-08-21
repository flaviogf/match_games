from marshmallow import EXCLUDE, fields, validate

from match_games import ma


class CreateGameStoreSerializer(ma.Schema):
    game_id = fields.Integer(required=True,
                             errors_message={'required': 'Game must be informed.'})
    store_id = fields.Integer(required=True,
                              errors_message={'required': 'Store must be informed.'})
    value = fields.Float(required=True,
                         errors_message={'required': 'Value must be informed.'})


create_game_store_serializer = CreateGameStoreSerializer(unknown=EXCLUDE)
