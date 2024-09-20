"""Auto migration on startup

Revision ID: db450c77143d
Revises: dae1f0468f9f
Create Date: 2024-09-20 21:21:51.721374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db450c77143d'
down_revision: Union[str, None] = 'dae1f0468f9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
