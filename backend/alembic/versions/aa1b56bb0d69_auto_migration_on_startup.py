"""Auto migration on startup

Revision ID: aa1b56bb0d69
Revises: 90103aa05e44
Create Date: 2024-09-20 21:19:39.802856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa1b56bb0d69'
down_revision: Union[str, None] = '90103aa05e44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
