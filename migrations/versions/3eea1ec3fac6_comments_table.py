"""comments table

Revision ID: 3eea1ec3fac6
Revises: 
Create Date: 2023-03-25 15:53:13.189655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eea1ec3fac6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recipe_api_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('None', 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key('None', 'recipe', ['recipe_api_id'], ['id'])
        batch_op.drop_column('recipe_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recipe_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'recipe', ['recipe_id'], ['id'])
        batch_op.drop_column('user_id')
        batch_op.drop_column('recipe_api_id')

    # ### end Alembic commands ###
