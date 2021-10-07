"""add profile url column to users table

Revision ID: a539c998cc1e
Revises: c194a2dc1240
Create Date: 2021-10-06 18:46:25.149618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a539c998cc1e'
down_revision = 'c194a2dc1240'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('profile_url', sa.String(length=320), nullable=True))


def downgrade():
    op.drop_column('users', 'profile_url')
