"""create table role

Revision ID: 2adbb177068b
Revises: 
Create Date: 2019-08-05 22:11:55.815304

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '2adbb177068b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('role',
                    sa.Column('id',
                              sa.Integer,
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False))


def downgrade():
    op.drop_table('role')
