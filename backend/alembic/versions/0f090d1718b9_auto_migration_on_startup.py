"""Auto migration on startup

Revision ID: 0f090d1718b9
Revises: 88be51098758
Create Date: 2024-09-20 21:20:51.758445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f090d1718b9'
down_revision: Union[str, None] = '88be51098758'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
