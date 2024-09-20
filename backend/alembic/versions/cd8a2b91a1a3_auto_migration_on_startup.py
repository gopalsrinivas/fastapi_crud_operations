"""Auto migration on startup

Revision ID: cd8a2b91a1a3
Revises: e3890a26ef31
Create Date: 2024-09-20 21:21:25.255307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd8a2b91a1a3'
down_revision: Union[str, None] = 'e3890a26ef31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
