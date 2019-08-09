from flask import Blueprint, render_template

blueprint = Blueprint('admin', __name__)


@blueprint.route('/admin/authentication')
def authentication():
    return render_template('admin/authentication.html')


@blueprint.route('/admin/stores')
def stores():
    return render_template('admin/stores.html')


@blueprint.route('/admin/games')
def games():
    return render_template('admin/games.html')
