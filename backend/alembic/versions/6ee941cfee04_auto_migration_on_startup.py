"""Auto migration on startup

Revision ID: 6ee941cfee04
Revises: 53b2860ea978
Create Date: 2024-09-20 21:21:02.313984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ee941cfee04'
down_revision: Union[str, None] = '53b2860ea978'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
