"""create table game_store

Revision ID: 39ae2529e047
Revises: e3f7856ccf39
Create Date: 2019-08-05 22:12:42.720660

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '39ae2529e047'
down_revision = 'e3f7856ccf39'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('game_store',
                    sa.Column('id',
                              sa.Integer,
                              primary_key=True),
                    sa.Column('store_id',
                              sa.Integer,
                              sa.ForeignKey('store.id')),
                    sa.Column('game_id',
                              sa.Integer,
                              sa.ForeignKey('game.id')))


def downgrade():
    op.drop_table('game_store')
