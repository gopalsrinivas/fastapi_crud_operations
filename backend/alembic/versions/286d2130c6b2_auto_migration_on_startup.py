"""Auto migration on startup

Revision ID: 286d2130c6b2
Revises: e6f87e846e35
Create Date: 2024-09-20 21:20:02.606960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '286d2130c6b2'
down_revision: Union[str, None] = 'e6f87e846e35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
