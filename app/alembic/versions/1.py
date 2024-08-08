"""Initial migration

Revision ID: 1
Revises: 
Create Date: 2024-07-25 03:01:05.940779
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1'
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
        sa.Column('km', sa.String(length=50), nullable=True),
        sa.Column('time', sa.String(length=50), nullable=True),
        sa.Column('price', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'client',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('fecha_llamada', sa.String(length=10), nullable=True),
        sa.Column('tipo_documento', sa.String(length=50), nullable=True),
        sa.Column('numero_documento', sa.String(length=50), nullable=True),
        sa.Column('nombres', sa.String(length=70), nullable=True),
        sa.Column('apellido', sa.String(length=70), nullable=True),
        sa.Column('fecha_nacimiento', sa.String(length=10), nullable=True),
        sa.Column('edad_en_anos', sa.Integer(), nullable=True),
        sa.Column('edad_en_meses', sa.Integer(), nullable=True),
        sa.Column('curso_vida', sa.String(length=50), nullable=True),
        sa.Column('regimen', sa.String(length=50), nullable=True),
        sa.Column('tipo_afiliado', sa.String(length=50), nullable=True),
        sa.Column('tipo_poblacion', sa.String(length=50), nullable=True),
        sa.Column('codigo_municipio', sa.String(length=50), nullable=True),
        sa.Column('nombre_municipio', sa.String(length=70), nullable=True),
        sa.Column('zona', sa.String(length=50), nullable=True),
        sa.Column('ips_atencion', sa.String(length=70), nullable=True),
        sa.Column('numero_telefono_reportado', sa.String(length=50), nullable=True),
        sa.Column('nombre_y_apellido_acudiente', sa.String(length=70), nullable=True),
        sa.Column('parentesco', sa.String(length=50), nullable=True),
        sa.Column('telefono_de_notificacion', sa.String(length=50), nullable=True),
        sa.Column('motivo_llamada_fallida', sa.String(length=100), nullable=True),
        sa.Column('observaciones', sa.String(length=255), nullable=True),
        sa.Column('approved', sa.Boolean, nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    # Drop tables
    op.drop_table('users')
    op.drop_table('taxi')
    op.drop_table('client')