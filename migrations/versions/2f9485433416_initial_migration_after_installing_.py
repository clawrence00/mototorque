"""Initial migration after installing flask-migrate

Revision ID: 2f9485433416
Revises: 
Create Date: 2023-08-03 21:40:28.229771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f9485433416'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dictionary', schema=None) as batch_op:
        batch_op.drop_constraint('dictionary_definition_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dictionary', schema=None) as batch_op:
        batch_op.create_unique_constraint('dictionary_definition_key', ['definition'])

    # ### end Alembic commands ###
