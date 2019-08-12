import secrets
from functools import partial

from flask import Blueprint, request

from match_games import db
from match_games.decorators import json, transational, upload, validate
from match_games.games.serializers import create_game_serializer
from match_games.models import Game

blueprint = Blueprint('games', __name__)


@blueprint.route('/api/v1/games', methods=['POST'])
@validate(create_game_serializer)
@transational()
@json()
@upload()
def create():
    body = request.form

    image_name = f'{secrets.token_hex(8)}.jpg'

    game = Game(name=body.get('name'),
                image=image_name)

    db.session.add(game)

    data = {
        'name': game.name,
        'image': game.image
    }

    return {'data': data, 'errors': []}, 201


@blueprint.route('/api/v1/games', methods=['GET'])
@transational()
@json()
def all_():
    limit = 10
    page = request.args.get('page', 1, type=int)
    offset = page * limit - limit

    games = Game.query.limit(limit).offset(offset).all()

    count = Game.query.count()

    data = [dict(id=game.id,
                 name=game.name,
                 image=game.image) for game in games]
    return {'data': data, 'errors': []}, 200, {'count': count}
