"""Auto migration on startup

Revision ID: 88be51098758
Revises: e7706b7b1a74
Create Date: 2024-09-20 21:20:46.358279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88be51098758'
down_revision: Union[str, None] = 'e7706b7b1a74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
