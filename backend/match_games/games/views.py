import secrets
from os.path import join

from flask import Blueprint, current_app, request, url_for

from match_games import db
from match_games.decorators import json, transational, validate
from match_games.games.serializers import create_game_serializer
from match_games.models import Game
from match_games.pagination import create_pagination

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
        image = files.get('image')
        _, extension = image.filename.split('.')
        game.image = f'{secrets.token_hex(8)}.{extension}'
        image_path = join(current_app.config.get('UPLOAD_DIR'), game.image)
        image.save(image_path)

    db.session.add(game)

    return {'data': None, 'errors': []}, 201


@blueprint.route('/api/v1/games', methods=['GET'])
@transational()
@json()
def all_():
    limit = 8
    page = request.args.get('page', 1, type=int)
    offset = page * limit - limit

    games = (Game.query
             .order_by(Game.name, Game.id)
             .limit(limit)
             .offset(offset)
             .all())

    pagination = create_pagination(page, Game.query.all())

    data = [dict(id=game.id,
                 name=game.name,
                 image=game.image,
                 image_path=url_for('static', filename=f'uploads/{game.image}', _external=True)) for game in games]

    return {'data': data, 'errors': []}, 200, pagination


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
        'image': game.image,
        'image_path': url_for('static', filename=f'uploads/{game.image}', _external=True),
        'stores': [dict(name=game_store.store.name,
                        value=game_store.value) for game_store in game.stores]
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
        image = files.get('image')
        _, extension = image.filename.split('.')
        game.image = f'{secrets.token_hex(8)}.{extension}'
        image_path = join(current_app.config.get('UPLOAD_DIR'), game.image)
        image.save(image_path)

    db.session.commit()

    return {'data': None, 'errors': []}, 200


@blueprint.route('/api/v1/games/<int:id>', methods=['DELETE'])
@transational()
@json()
def destroy(id):
    game = Game.query.filter(Game.id == id).first()

    if not game:
        return {'data': None, 'errors': ['Game with this id not exists.']}, 404

    db.session.delete(game)

    return {'data': None, 'errors': []}, 200
