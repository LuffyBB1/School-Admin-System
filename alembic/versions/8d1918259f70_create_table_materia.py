"""Create table materia

Revision ID: 8d1918259f70
Revises: 17ff0541a6c5
Create Date: 2024-03-01 19:19:20.878558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d1918259f70'
down_revision: Union[str, None] = '17ff0541a6c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    
    op.create_table(
        'salon',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cod_salon', sa.String, unique=True),
    )
    
    # Estudiante
    op.create_table(
        'estudiante',
        sa.Column('documento', sa.Integer, primary_key=True, unique=True),
        sa.Column('nombre', sa.String, nullable=False),
        sa.Column('apellido', sa.String, nullable=False),
        sa.Column('edad', sa.Integer, nullable=False),
        sa.Column('fecha_nacimiento', sa.Date, nullable=False),
        sa.Column('jornada', sa.String, nullable=False),
        sa.Column('salon_id', sa.String, sa.ForeignKey('salon.cod_salon')),
    )

    # Asistencia
    op.create_table(
        'asistencia',
        sa.Column('id_asistencia', sa.Integer, primary_key=True),
        sa.Column('asiste', sa.Boolean, default=False),
        sa.Column('ausente', sa.Boolean, default=False),
        sa.Column('fecha', sa.Date, nullable=False),
        sa.Column('id_estudiante', sa.Integer, sa.ForeignKey('estudiante.documento')),
        sa.Column('cod_salon', sa.String, sa.ForeignKey('salon.cod_salon')),
    )

    # Materia
    op.create_table(
        'materia',
        sa.Column('id_materia', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String, nullable=False),
        sa.Column('cod_salon', sa.String, sa.ForeignKey('salon.cod_salon')),
    )

def downgrade():
    op.drop_table('materia')
    op.drop_table('asistencia')
    op.drop_table('estudiante')
    op.drop_table('salon')
