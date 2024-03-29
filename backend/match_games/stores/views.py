import secrets
from os.path import join

from flask import Blueprint, current_app, request, url_for

from match_games import db
from match_games.decorators import json, transational, validate
from match_games.models import Store
from match_games.pagination import create_pagination
from match_games.stores.serializers import create_store_serializer

blueprint = Blueprint('stores', __name__)


@blueprint.route('/api/v1/stores', methods=['POST'])
@validate(create_store_serializer)
@transational()
@json()
def create():
    files = request.files
    body = request.form

    store = Store(name=body.get('name'))

    if files:
        image = files.get('image')
        _, extension = image.filename.split('.')
        store.image = f'{secrets.token_hex(8)}.{extension}'
        image_path = join(current_app.config.get('UPLOAD_DIR'), store.image)
        image.save(image_path)

    db.session.add(store)

    return {'data': None, 'errors': []}, 201


@blueprint.route('/api/v1/stores', methods=['GET'])
@transational()
@json()
def all_():
    limit = 8
    page = request.args.get('page', 1, type=int)
    offset = page * limit - limit

    stores = (Store.query
              .order_by(Store.name, Store.id)
              .limit(limit)
              .offset(offset)
              .all())

    stores = [dict(id=store.id,
                   name=store.name,
                   image=store.image,
                   image_path=url_for('static', filename=f'uploads/{store.image}', _external=True))
              for store in stores]

    pagination = create_pagination(page, Store.query.all())

    return {'data': stores, 'errors': []}, 200, pagination


@blueprint.route('/api/v1/stores/<int:id>', methods=['GET'])
@transational()
@json()
def single(id):
    store = Store.query.filter(Store.id == id).first()

    if not store:
        return {'data': '', 'errors': ['Store with this id not exists.']}, 404

    data = {
        'id': store.id,
        'name': store.name,
        'image': store.image,
        'image_path': url_for('static', filename=f'uploads/{store.image}', _external=True)
    }

    return {'data': data, 'errors': []}, 200


@blueprint.route('/api/v1/stores/<int:id>', methods=['PUT'])
@validate(create_store_serializer)
@transational()
@json()
def update(id):
    files = request.files
    body = request.form

    store = Store.query.filter(Store.id == id).first()

    if not store:
        return {'data': None, 'errors': ['Game with this id not exists']}, 404

    store.name = body.get('name')

    if files:
        image = files.get('image')
        _, extension = image.filename.split('.')
        store.image = f'{secrets.token_hex(8)}.{extension}'
        image_path = join(current_app.config.get('UPLOAD_DIR'), store.image)
        image.save(image_path)

    db.session.commit()

    return {'data': None, 'errors': []}, 200


@blueprint.route('/api/v1/stores/<int:id>', methods=['DELETE'])
@transational()
@json()
def destroy(id):
    store = Store.query.filter(Store.id == id).first()

    if not store:
        return {'data': None, 'errors': ['Game with this id not exists.']}, 404

    db.session.delete(store)

    return {'data': None, 'errors': []}, 200
