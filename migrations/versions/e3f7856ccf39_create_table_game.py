"""create table game

Revision ID: e3f7856ccf39
Revises: 293f3656c888
Create Date: 2019-08-05 22:12:30.690992

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'e3f7856ccf39'
down_revision = '293f3656c888'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('game',
                    sa.Column('id',
                              sa.Integer,
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False),
                    sa.Column('image',
                              sa.String(250),
                              nullable=False))


def downgrade():
    op.drop_table('game')
