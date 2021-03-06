"""achieve migrations

Revision ID: 256b4b704335
Revises: b352aa7f2736
Create Date: 2020-02-20 16:31:22.441182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '256b4b704335'
down_revision = 'b352aa7f2736'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('qoutes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('qoutes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('quote', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('author', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='qoutes_pkey')
    )
    # ### end Alembic commands ###
