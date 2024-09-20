"""Auto migration on startup

Revision ID: 90103aa05e44
Revises: d0c94729f657
Create Date: 2024-09-20 21:19:34.770366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90103aa05e44'
down_revision: Union[str, None] = 'd0c94729f657'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
