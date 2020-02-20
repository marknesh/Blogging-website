"""migrate accordinly

Revision ID: 872aeeaf3243
Revises: 
Create Date: 2020-02-20 15:19:06.224857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872aeeaf3243'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogs_users_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'users_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('blogs_users_id_fkey', 'blogs', 'person', ['users_id'], ['id'])
    # ### end Alembic commands ###
