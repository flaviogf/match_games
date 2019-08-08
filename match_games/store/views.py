from flask import Blueprint, render_template

from match_games import db
from match_games.models import Store
from match_games.store.forms import CreateStoreForm
from match_games.utils import upload

blueprint = Blueprint('store', __name__)


@blueprint.route('/admin/store/create', methods=['GET', 'POST'])
def create():
    form = CreateStoreForm()

    if form.validate_on_submit():
        store = Store(name=form.name.data,
                      image=upload(form.image.data))
        db.session.add(store)
        db.session.commit()
        return 'OK'

    return render_template('store/create.html', form=form)
