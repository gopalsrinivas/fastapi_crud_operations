"""Auto migration on startup

Revision ID: 645afe923dc4
Revises: 6cc113ad69af
Create Date: 2024-09-20 21:22:02.291118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '645afe923dc4'
down_revision: Union[str, None] = '6cc113ad69af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
