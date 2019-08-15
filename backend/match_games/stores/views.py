import secrets
from os.path import join

from flask import Blueprint, current_app, request

from match_games import db, q
from match_games.decorators import json, transational, validate
from match_games.models import Store
from match_games.stores.serializers import create_store
from match_games.tasks import compress_image
from match_games.pagination import create_pagination

blueprint = Blueprint('stores', __name__)


@blueprint.route('/api/v1/stores', methods=['POST'])
@validate(create_store)
@transational()
@json()
def create():
    files = request.files
    body = request.form

    store = Store(name=body.get('name'))

    if files:
        store.image = f'{secrets.token_hex(8)}.jpg'
        image_path = join(current_app.config.get('UPLOAD_DIR'), store.image)
        files.get('image').save(image_path)
        q.enqueue(compress_image, image_path)

    db.session.add(store)

    return {'data': None, 'errors': []}, 201


@blueprint.route('/api/v1/stores', methods=['GET'])
def all_():
    limit = 8
    page = request.args.get('page', 1, type=int)
    offset = page * limit - limit

    stores = (Store.query
              .order_by(Store.name)
              .limit(limit)
              .offset(offset)
              .all())

    stores = [dict(id=store.id,
                   name=store.name,
                   image=store.image)
              for store in stores]

    pagination = create_pagination(page, Store.query.all())

    return {'data': stores, 'errors': []}, 200, pagination
