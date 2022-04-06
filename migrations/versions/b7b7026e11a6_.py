"""empty message

Revision ID: b7b7026e11a6
Revises: 6a68f2b6e75a
Create Date: 2019-03-02 20:14:35.237330

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b7b7026e11a6'
down_revision = '6a68f2b6e75a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'last_update',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'last_update',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
