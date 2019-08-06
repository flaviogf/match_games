"""create table user

Revision ID: eac3a0bba4b5
Revises: 2adbb177068b
Create Date: 2019-08-05 22:12:07.531765

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'eac3a0bba4b5'
down_revision = '2adbb177068b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id',
                              sa.Integer,
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False),
                    sa.Column('email',
                              sa.String(250),
                              nullable=False,
                              unique=True),
                    sa.Column('password',
                              sa.String(250),
                              nullable=False),
                    sa.Column('image',
                              sa.String(250),
                              nullable=False),
                    sa.Column('role_id',
                              sa.Integer,
                              sa.ForeignKey('role.id')))


def downgrade():
    op.drop_table('user')
