"""Auto migration on startup

Revision ID: 2cd658418038
Revises: 45437d0c38c5
Create Date: 2024-09-20 21:22:14.056222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2cd658418038'
down_revision: Union[str, None] = '45437d0c38c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
