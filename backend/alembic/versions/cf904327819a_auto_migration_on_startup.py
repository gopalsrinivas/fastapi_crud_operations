"""Auto migration on startup

Revision ID: cf904327819a
Revises: 88e4c4061b08
Create Date: 2024-09-20 21:22:31.538361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf904327819a'
down_revision: Union[str, None] = '88e4c4061b08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
