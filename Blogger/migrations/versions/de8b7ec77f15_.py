"""empty message

Revision ID: de8b7ec77f15
Revises: 131e7e79afcb
Create Date: 2020-12-12 00:40:46.869414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de8b7ec77f15'
down_revision = '131e7e79afcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('alt_phone_no', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contacts', 'alt_phone_no')
    # ### end Alembic commands ###
