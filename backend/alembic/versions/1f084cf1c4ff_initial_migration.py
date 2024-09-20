"""Initial migration

Revision ID: 1f084cf1c4ff
Revises: 
Create Date: 2024-09-20 15:50:44.698112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1f084cf1c4ff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('notes', sa.Column('created_on', sa.DateTime(),
                  nullable=True))  # Initially nullable
    op.add_column('notes', sa.Column(
        'updated_on', sa.DateTime(), nullable=True))
    op.drop_column('notes', 'date_created')

    # Set default values or update existing rows
    op.execute("UPDATE notes SET created_on = NOW() WHERE created_on IS NULL")

    # Alter column to be non-nullable after updating existing rows
    op.alter_column('notes', 'created_on', nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('date_created',
                  postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('notes', 'updated_on')
    op.drop_column('notes', 'created_on')
    op.drop_column('notes', 'is_active')
    # ### end Alembic commands ###
