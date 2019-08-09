from flask import Blueprint

blueprint = Blueprint('stores', __name__)


@blueprint.route('/stores')
def stores():
    return 'OK'
