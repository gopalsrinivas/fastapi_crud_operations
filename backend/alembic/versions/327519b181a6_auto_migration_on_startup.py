"""Auto migration on startup

Revision ID: 327519b181a6
Revises: 2e56506940ea
Create Date: 2024-09-20 21:20:14.218713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '327519b181a6'
down_revision: Union[str, None] = '2e56506940ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
