"""create table game

Revision ID: aeab08c9fd34
Revises: a81e5dd18927
Create Date: 2019-08-11 16:59:53.968757

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'aeab08c9fd34'
down_revision = 'a81e5dd18927'
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
                              nullable=False,
                              default='default.jpg'))


def downgrade():
    op.drop_table('game')
