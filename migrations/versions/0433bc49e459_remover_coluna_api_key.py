"""remover coluna api_key

Revision ID: 0433bc49e459
Revises: 0ca818d45f9e
Create Date: 2022-02-23 22:32:47.899660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0433bc49e459'
down_revision = '0ca818d45f9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'api_key')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('api_key', sa.VARCHAR(length=511), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
