"""empty message

Revision ID: 146af105c8ed
Revises: None
Create Date: 2015-07-27 10:36:58.984498

"""

# revision identifiers, used by Alembic.
revision = '146af105c8ed'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rgb_r', sa.Integer(), nullable=True),
    sa.Column('rgb_g', sa.Integer(), nullable=True),
    sa.Column('rgb_b', sa.Integer(), nullable=True),
    sa.Column('lab_l', sa.Float(), nullable=True),
    sa.Column('lab_a', sa.Float(), nullable=True),
    sa.Column('lab_b', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('color')
    ### end Alembic commands ###