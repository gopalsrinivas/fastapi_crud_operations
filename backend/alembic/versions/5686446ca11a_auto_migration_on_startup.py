"""Auto migration on startup

Revision ID: 5686446ca11a
Revises: aa1b56bb0d69
Create Date: 2024-09-20 21:19:45.071358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5686446ca11a'
down_revision: Union[str, None] = 'aa1b56bb0d69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
