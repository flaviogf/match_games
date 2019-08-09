from flask import Flask, jsonify, render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    bcrypt.init_app(app)

    from match_games import admin
    app.register_blueprint(admin.views.blueprint)
    from match_games import games
    app.register_blueprint(games.views.blueprint)
    from match_games import stores
    app.register_blueprint(stores.views.blueprint)

    @app.errorhandler(404)
    def error_404(ex):
        return jsonify({'data': None, 'errors': ['Not found.']}), 404

    @app.errorhandler(500)
    def error_500(ex):
        return jsonify({'data': None, 'errors': ['Internal server error.']}), 500

    @app.route('/')
    def index():
        return render_template('index.html')

    from match_games import commands
    app.cli.add_command(commands.create_roles)
    app.cli.add_command(commands.create_admin)

    return app
