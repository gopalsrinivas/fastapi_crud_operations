"""Auto migration on startup

Revision ID: d0c94729f657
Revises: 32dd50feb7f0
Create Date: 2024-09-20 21:19:29.252502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0c94729f657'
down_revision: Union[str, None] = '32dd50feb7f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
