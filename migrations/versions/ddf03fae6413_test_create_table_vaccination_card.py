"""test create table vaccination_card

Revision ID: ddf03fae6413
Revises: 
Create Date: 2022-02-09 10:11:35.256387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddf03fae6413'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccine_cards',
    sa.Column('cpf', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('first_shot_date', sa.Date(), nullable=True),
    sa.Column('second_shot_date', sa.Date(), nullable=True),
    sa.Column('vaccine_name', sa.String(), nullable=False),
    sa.Column('health_unity_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_cards')
    # ### end Alembic commands ###
