from flask import Blueprint, render_template

from match_games.admin.forms import AuthenticateForm

blueprint = Blueprint('admin', __name__)


@blueprint.route('/admin', methods=['GET', 'POST'])
def authenticate():
    form = AuthenticateForm()

    form.validate_on_submit()

    return render_template('admin/authenticate.html', form=form)
