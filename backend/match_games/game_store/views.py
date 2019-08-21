from flask import Blueprint, request

from match_games import db
from match_games.decorators import json, transational, validate
from match_games.game_store.serializers import create_game_store_serializer
from match_games.models import Game, GameStore, Store
from match_games.pagination import create_pagination

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


@blueprint.route('/api/v1/game-store', methods=['GET'])
@transational()
@json()
def all_():
    page = request.args.get('page', 1, type=int)
    limit = 8
    offset = page * limit - limit

    list_game_store = (GameStore.query
                       .join(Game)
                       .join(Store)
                       .order_by(Game.name, Store.name, Game.id)
                       .limit(limit)
                       .offset(offset)
                       .all())

    list_game_store = [dict(store=game_store.store.name,
                            game=game_store.game.name,
                            value=game_store.value) for game_store in list_game_store]

    pagination = create_pagination(page, GameStore.query.all())

    return {'data': list_game_store, 'errors': []}, 200, pagination
