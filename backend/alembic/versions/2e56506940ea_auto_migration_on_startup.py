"""Auto migration on startup

Revision ID: 2e56506940ea
Revises: 286d2130c6b2
Create Date: 2024-09-20 21:20:09.079641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e56506940ea'
down_revision: Union[str, None] = '286d2130c6b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
