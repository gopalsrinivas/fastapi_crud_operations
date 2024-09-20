"""Auto migration on startup

Revision ID: b4c2edf29ec5
Revises: 5686446ca11a
Create Date: 2024-09-20 21:19:51.503327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4c2edf29ec5'
down_revision: Union[str, None] = '5686446ca11a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
