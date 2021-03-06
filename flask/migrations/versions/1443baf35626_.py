"""empty message

Revision ID: 1443baf35626
Revises: c85c0316f630
Create Date: 2021-01-16 11:08:47.205600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1443baf35626'
down_revision = 'c85c0316f630'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('videos', sa.String(length=30000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.drop_column('videos')

    # ### end Alembic commands ###
