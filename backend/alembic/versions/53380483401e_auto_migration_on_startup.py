"""Auto migration on startup

Revision ID: 53380483401e
Revises: 00bd68450378
Create Date: 2024-09-20 21:20:29.628758

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53380483401e'
down_revision: Union[str, None] = '00bd68450378'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
