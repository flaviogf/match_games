"""create table user

Revision ID: a81e5dd18927
Revises: 
Create Date: 2019-08-10 13:31:22.349098

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a81e5dd18927'
down_revision = None
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
                              nullable=False),
                    sa.Column('password',
                              sa.String(250),
                              nullable=False),
                    sa.Column('image',
                              sa.String(250),
                              nullable=False,
                              default='default.jpg'),
                    sa.Column('role',
                              sa.String(250),
                              nullable=False))


def downgrade():
    op.drop_table('user')
