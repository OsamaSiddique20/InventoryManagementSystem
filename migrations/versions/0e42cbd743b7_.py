"""empty message

Revision ID: 0e42cbd743b7
Revises: 
Create Date: 2023-11-15 22:01:21.007637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e42cbd743b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Category',
    sa.Column('cat_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cat_name', sa.String(length=255), nullable=False),
    sa.Column('cat_desc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('cat_id')
    )
    op.create_table('holder',
    sa.Column('holder_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('location', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('holder_id')
    )
    op.create_table('item',
    sa.Column('item_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=225), nullable=False),
    sa.Column('category_cat_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_cat_id'], ['Category.cat_id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('holder_has_item',
    sa.Column('holder_holder_id', sa.Integer(), nullable=False),
    sa.Column('item_item_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.String(length=45), nullable=True),
    sa.Column('serial_num', sa.String(length=45), nullable=True),
    sa.ForeignKeyConstraint(['holder_holder_id'], ['holder.holder_id'], ),
    sa.ForeignKeyConstraint(['item_item_id'], ['item.item_id'], ),
    sa.PrimaryKeyConstraint('holder_holder_id', 'item_item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('holder_has_item')
    op.drop_table('item')
    op.drop_table('holder')
    op.drop_table('Category')
    # ### end Alembic commands ###
