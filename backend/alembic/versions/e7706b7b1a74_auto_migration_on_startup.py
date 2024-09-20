"""Auto migration on startup

Revision ID: e7706b7b1a74
Revises: 84bcb31835d0
Create Date: 2024-09-20 21:20:41.252228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7706b7b1a74'
down_revision: Union[str, None] = '84bcb31835d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
