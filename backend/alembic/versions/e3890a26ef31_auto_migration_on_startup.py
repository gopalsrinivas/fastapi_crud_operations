"""Auto migration on startup

Revision ID: e3890a26ef31
Revises: 090ef2ce145c
Create Date: 2024-09-20 21:21:19.534178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3890a26ef31'
down_revision: Union[str, None] = '090ef2ce145c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
