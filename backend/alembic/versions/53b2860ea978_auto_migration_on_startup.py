"""Auto migration on startup

Revision ID: 53b2860ea978
Revises: 0f090d1718b9
Create Date: 2024-09-20 21:20:57.482406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53b2860ea978'
down_revision: Union[str, None] = '0f090d1718b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
