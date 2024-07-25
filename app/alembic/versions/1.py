"""Initial migration

Revision ID: <revision_id>
Revises: 
Create Date: 2024-07-25 03:01:05.940779
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create tables
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('username', sa.String(length=50), nullable=True),
        sa.Column('name', sa.String(length=70), nullable=True),
        sa.Column('email', sa.String(length=50), nullable=True),
        sa.Column('hashed_password', sa.String(length=70), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )
    op.create_table(
        'taxi',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('town', sa.String(length=50), nullable=True),
        sa.Column('kilometers', sa.String(length=50), nullable=True),
        sa.Column('time', sa.String(length=50), nullable=True),
        sa.Column('price', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('town'),
        sa.UniqueConstraint('kilometers'),
        sa.UniqueConstraint('time'),
        sa.UniqueConstraint('price')
    )

def downgrade() -> None:
    # Drop tables
    op.drop_table('users')
    op.drop_table('taxi')