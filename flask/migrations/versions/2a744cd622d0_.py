"""empty message

Revision ID: 2a744cd622d0
Revises: 1443baf35626
Create Date: 2021-01-16 11:19:23.757362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a744cd622d0'
down_revision = '1443baf35626'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contact', sa.String(length=5000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.drop_column('contact')

    # ### end Alembic commands ###