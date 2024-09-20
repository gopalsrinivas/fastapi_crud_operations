"""Auto migration on startup

Revision ID: e6f87e846e35
Revises: b4c2edf29ec5
Create Date: 2024-09-20 21:19:57.375218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6f87e846e35'
down_revision: Union[str, None] = 'b4c2edf29ec5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
