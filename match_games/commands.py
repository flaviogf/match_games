import click
from flask.cli import with_appcontext

from match_games import bcrypt, db
from match_games.models import Role, User


@click.command('create-roles', help='Create default roles.')
@with_appcontext
def create_roles():
    if Role.query.count():
        click.secho('Roles already created.', fg='yellow')
        return

    db.session.add(Role(name='admin'))
    db.session.add(Role(name='default'))
    db.session.add(Role(name='anonymous'))

    db.session.commit()

    click.secho('Roles has been created.', fg='blue')


@click.command('create-admin', help='Create default admin.')
@with_appcontext
def create_admin():
    if not Role.query.count():
        click.secho('You must create the roles first.', fg='yellow')
        return

    if User.query.filter_by(email='admin').first():
        click.secho('Admin already created.', fg='yellow')
        return

    role = Role.query.first()

    password = bcrypt.generate_password_hash('admin').decode('utf-8')

    db.session.add(User(name='admin',
                        email='admin',
                        password=password,
                        role_id=role.id))

    db.session.commit()

    click.secho('Admin has been created.', fg='blue')
