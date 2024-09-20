"""Auto migration on startup

Revision ID: 45437d0c38c5
Revises: 645afe923dc4
Create Date: 2024-09-20 21:22:07.661213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45437d0c38c5'
down_revision: Union[str, None] = '645afe923dc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
