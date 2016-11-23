"""add ReleaseMonitor.added_to_library

Revision ID: 36bd688b04b
Revises: 4af79c08de
Create Date: 2014-11-06 08:25:44.563626

"""

# revision identifiers, used by Alembic.
revision = '36bd688b04b'
down_revision = '4af79c08de'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('release_monitor', sa.Column('added_to_library', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('release_monitor', 'added_to_library')
    ### end Alembic commands ###
