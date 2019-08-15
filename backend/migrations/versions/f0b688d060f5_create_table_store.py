"""create table store

Revision ID: f0b688d060f5
Revises: aeab08c9fd34
Create Date: 2019-08-15 15:31:15.641851

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f0b688d060f5'
down_revision = 'aeab08c9fd34'
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
                              nullable=False,
                              default='default.jpg'))


def downgrade():
    op.drop_table('store')
