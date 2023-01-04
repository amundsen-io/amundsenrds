"""add table/column lineage

Revision ID: aa30b4276b9b
Revises: a539c998cc1e
Create Date: 2023-01-03 14:48:38.280768

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'aa30b4276b9b'
down_revision = 'a539c998cc1e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # add table/column lineage tables
    op.create_table('table_lineage',
    sa.Column('table_source_rk', sa.String(length=1024, collation='latin1_general_cs'), nullable=False),
    sa.Column('table_target_rk', sa.String(length=1024, collation='latin1_general_cs'), nullable=False),
    sa.Column('published_tag', sa.String(length=128), nullable=False),
    sa.Column('publisher_last_updated_epoch_ms', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['table_source_rk'], ['table_metadata.rk'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['table_target_rk'], ['table_metadata.rk'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('table_source_rk', 'table_target_rk')
    )
    op.create_table('column_lineage',
    sa.Column('column_source_rk', sa.String(length=1024, collation='latin1_general_cs'), nullable=False),
    sa.Column('column_target_rk', sa.String(length=1024, collation='latin1_general_cs'), nullable=False),
    sa.Column('published_tag', sa.String(length=128), nullable=False),
    sa.Column('publisher_last_updated_epoch_ms', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['column_source_rk'], ['column_metadata.rk'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['column_target_rk'], ['column_metadata.rk'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('column_source_rk', 'column_target_rk')
    )


def downgrade() -> None:
    # drop table/lineage tables
    op.drop_table('column_lineage')
    op.drop_table('table_lineage')
