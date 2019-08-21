from flask import Blueprint, request

from match_games import db
from match_games.decorators import json, transational, validate
from match_games.game_store.serializers import create_game_store_serializer
from match_games.models import GameStore

blueprint = Blueprint('game_store', __name__)


@blueprint.route('/api/v1/game-store', methods=['POST'])
@validate(create_game_store_serializer)
@transational()
@json()
def create():
    body = request.json

    game_store = GameStore(game_id=body.get('game_id'),
                           store_id=body.get('store_id'),
                           value=body.get('value'))

    db.session.add(game_store)

    return {'data': None, 'errors': []}, 200
