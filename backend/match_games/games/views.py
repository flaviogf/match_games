import secrets
from os.path import join

from flask import Blueprint, current_app, request
from PIL import Image

from match_games import db, q
from match_games.decorators import json, transational, validate
from match_games.games.serializers import create_game_serializer
from match_games.models import Game

blueprint = Blueprint('games', __name__)


@blueprint.route('/api/v1/games', methods=['POST'])
@validate(create_game_serializer)
@transational()
@json()
def create():
    files = request.files
    body = request.form

    game = Game(name=body.get('name'))

    if files:
        image_name = f'{secrets.token_hex(8)}.jpg'
        upload_dir = current_app.config.get('UPLOAD_DIR')
        image_path = join(upload_dir, image_name)
        image = Image.open(files.get('image'))
        image.thumbnail((100, 100))
        image.save(image_path)
        game.image = image_name

    db.session.add(game)

    return {'data': None, 'errors': []}, 201


@blueprint.route('/api/v1/games', methods=['GET'])
@transational()
@json()
def all_():
    limit = 10
    page = request.args.get('page', 1, type=int)
    offset = page * limit - limit

    games = (Game.query
             .order_by(Game.name)
             .limit(limit)
             .offset(offset)
             .all())

    count = Game.query.count()

    data = [dict(id=game.id,
                 name=game.name,
                 image=game.image) for game in games]
    return {'data': data, 'errors': []}, 200, {'count': count}


@blueprint.route('/api/v1/games/<int:id>', methods=['GET'])
@transational()
@json()
def single(id):
    game = Game.query.filter(Game.id == id).first()

    if not game:
        return {'data': None, 'errors': ['Game with this id not exists.']}, 404

    data = {
        'id': game.id,
        'name': game.name,
        'image': game.image
    }

    return {'data': data, 'errors': []}, 200


@blueprint.route('/api/v1/games/<int:id>', methods=['PUT'])
@validate(create_game_serializer)
@transational()
@json()
def update(id):
    files = request.files
    body = request.form

    game = Game.query.filter(Game.id == id).first()

    if not game:
        return {'data': None, 'errors': ['Game with this id not exists.']}, 404

    game.name = body.get('name')

    if files:
        image_name = f'{secrets.token_hex(8)}.jpg'
        upload_dir = current_app.config.get('UPLOAD_DIR')
        image_path = join(upload_dir, image_name)
        image = Image.open(files.get('image'))
        image.thumbnail((100, 100))
        image.save(image_path)
        game.image = image_name

    db.session.commit()

    return {'data': None, 'errors': []}, 200
