"""create db

Revision ID: 7ab69a611d9e
Revises: e36e6de446c3
Create Date: 2020-07-07 11:32:29.604052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab69a611d9e'
down_revision = 'e36e6de446c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('sno', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('phone_no', sa.String(length=10), nullable=False),
    sa.Column('msg', sa.String(length=120), nullable=False),
    sa.Column('date', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('sno')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('posts',
    sa.Column('sno', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('slug', sa.String(length=25), nullable=False),
    sa.Column('content', sa.String(length=400), nullable=False),
    sa.Column('tagline', sa.String(length=120), nullable=False),
    sa.Column('date', sa.String(length=12), nullable=True),
    sa.Column('img_name', sa.String(length=20), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('sno'),
    sa.UniqueConstraint('slug')
    )
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_table('posts')
    op.drop_table('user')
    op.drop_table('contacts')
    # ### end Alembic commands ###
