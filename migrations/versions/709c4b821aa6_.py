"""empty message

Revision ID: 709c4b821aa6
Revises: 750fbeb016c5
Create Date: 2021-04-02 17:17:34.347423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '709c4b821aa6'
down_revision = '750fbeb016c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.Column('coin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['coin_id'], ['coin.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
