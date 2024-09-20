"""Auto migration on startup

Revision ID: 22bb3045d7ee
Revises: b769b739a39d
Create Date: 2024-09-20 21:21:41.336931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22bb3045d7ee'
down_revision: Union[str, None] = 'b769b739a39d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
