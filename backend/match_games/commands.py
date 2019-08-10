import click
from flask.cli import with_appcontext

from match_games import bcrypt, db
from match_games.models import User


@click.command('create-admin', help='Create the admin user.')
@with_appcontext
def create_admin():
    if User.query.filter(User.email == 'admin@admin.com').first():
        click.secho('Admin has already created.', fg='yellow')
        return

    password_hash = bcrypt.generate_password_hash('admin').decode('utf-8')

    admin = User(name='admin',
                 email='admin@admin.com',
                 password=password_hash,
                 role='admin')

    db.session.add(admin)
    db.session.commit()

    click.secho('Admin has been created.', fg='blue')
