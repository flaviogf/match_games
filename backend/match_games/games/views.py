import secrets

from flask import Blueprint, request

from match_games import db
from match_games.decorators import json, transational, validate, upload
from match_games.games.serializers import create_game_serializer
from match_games.models import Game

blueprint = Blueprint('games', __name__)


@blueprint.route('/api/v1/games', methods=['POST'])
@validate(create_game_serializer)
@transational()
@json()
@upload()
def index():
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
