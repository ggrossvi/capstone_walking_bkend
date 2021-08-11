"""updated model

Revision ID: a06c82e1a32a
Revises: b83615784002
Create Date: 2021-08-11 11:27:44.596060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a06c82e1a32a'
down_revision = 'b83615784002'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('buddy', sa.Column('address', sa.Text(), nullable=True))
    op.add_column('buddy', sa.Column('apt', sa.Text(), nullable=True))
    op.add_column('buddy', sa.Column('city', sa.Text(), nullable=True))
    op.add_column('buddy', sa.Column('first_name', sa.Text(), nullable=True))
    op.add_column('buddy', sa.Column('last_name', sa.Text(), nullable=True))
    op.add_column('buddy', sa.Column('state', sa.Text(), nullable=True))
    op.drop_column('buddy', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('buddy', sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('buddy', 'state')
    op.drop_column('buddy', 'last_name')
    op.drop_column('buddy', 'first_name')
    op.drop_column('buddy', 'city')
    op.drop_column('buddy', 'apt')
    op.drop_column('buddy', 'address')
    # ### end Alembic commands ###