"""Auto migration on startup

Revision ID: 84bcb31835d0
Revises: 53380483401e
Create Date: 2024-09-20 21:20:35.655395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84bcb31835d0'
down_revision: Union[str, None] = '53380483401e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
