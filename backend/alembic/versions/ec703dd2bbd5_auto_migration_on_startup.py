"""Auto migration on startup

Revision ID: ec703dd2bbd5
Revises: 2cd658418038
Create Date: 2024-09-20 21:22:19.540883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec703dd2bbd5'
down_revision: Union[str, None] = '2cd658418038'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
