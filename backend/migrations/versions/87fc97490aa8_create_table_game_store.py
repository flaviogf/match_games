"""create table game_store

Revision ID: 87fc97490aa8
Revises: f0b688d060f5
Create Date: 2019-08-21 16:41:06.723179

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '87fc97490aa8'
down_revision = 'f0b688d060f5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('game_store',
                    sa.Column('game_id',
                              sa.Integer,
                              sa.ForeignKey('game.id'),
                              primary_key=True),
                    sa.Column('store_id',
                              sa.Integer,
                              sa.ForeignKey('store.id'),
                              primary_key=True),
                    sa.Column('value',
                              sa.Float,
                              nullable=False))


def downgrade():
    op.drop_table('game_store')
