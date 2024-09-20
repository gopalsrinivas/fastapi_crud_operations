"""Auto migration on startup

Revision ID: dae1f0468f9f
Revises: 22bb3045d7ee
Create Date: 2024-09-20 21:21:46.999020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dae1f0468f9f'
down_revision: Union[str, None] = '22bb3045d7ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
