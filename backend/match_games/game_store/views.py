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

    game_id = body.get('game_id')
    store_id = body.get('store_id')

    game_store = (GameStore.query
                  .filter(GameStore.game_id == game_id, GameStore.store_id == store_id)
                  .first())

    if game_store:
        return {'data': None, 'errors': ['Game already exists in this store.']}, 400

    game_store = GameStore(game_id=game_id,
                           store_id=store_id,
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

    list_game_store = [dict(id=game_store.id,
                            store=game_store.store.name,
                            game=game_store.game.name,
                            value=game_store.value) for game_store in list_game_store]

    pagination = create_pagination(page, GameStore.query.all())

    return {'data': list_game_store, 'errors': []}, 200, pagination


@blueprint.route('/api/v1/game-store/<int:id>', methods=['GET'])
@transational()
@json()
def single(id):
    game_store = GameStore.query.filter(GameStore.id == id).first()

    if not game_store:
        return {'data': None, 'errors': ['Game store with that id not exists.']}, 404

    game_store = {
        'store_id': game_store.store.id,
        'store': game_store.store.name,
        'game_id': game_store.game.id,
        'game': game_store.game.name,
        'value': game_store.value
    }

    return {'data': game_store, 'errors': []}, 200


@blueprint.route('/api/v1/game-store/<int:id>', methods=['PUT'])
@validate(create_game_store_serializer)
@transational()
@json()
def update(id):
    game_store = (GameStore.query.filter(GameStore.id == id).first())

    if not game_store:
        return {'data': None, 'errors': []}, 404

    game_store.game_id = request.json.get('game_id')
    game_store.store_id = request.json.get('store_id')
    game_store.value = request.json.get('value')

    return {'data': None, 'errors': []}, 200


@blueprint.route('/api/v1/game-store/<int:id>', methods=['DELETE'])
@transational()
@json()
def destroy(id):
    game_store = GameStore.query.filter(GameStore.id == id).first()

    if not game_store:
        return {'data': None, 'errors': []}, 404

    db.session.delete(game_store)

    return {'data': None, 'errors': []}, 200
