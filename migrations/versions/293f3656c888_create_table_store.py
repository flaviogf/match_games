"""create table store

Revision ID: 293f3656c888
Revises: eac3a0bba4b5
Create Date: 2019-08-05 22:12:20.316616

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '293f3656c888'
down_revision = 'eac3a0bba4b5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('store',
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
    op.drop_table('store')
