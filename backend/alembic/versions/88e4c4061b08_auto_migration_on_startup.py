"""Auto migration on startup

Revision ID: 88e4c4061b08
Revises: ec703dd2bbd5
Create Date: 2024-09-20 21:22:25.516398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88e4c4061b08'
down_revision: Union[str, None] = 'ec703dd2bbd5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
