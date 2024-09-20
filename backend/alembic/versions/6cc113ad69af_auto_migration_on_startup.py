"""Auto migration on startup

Revision ID: 6cc113ad69af
Revises: db450c77143d
Create Date: 2024-09-20 21:21:56.647295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cc113ad69af'
down_revision: Union[str, None] = 'db450c77143d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
