"""Auto migration on startup

Revision ID: 06a82c13584e
Revises: cd8a2b91a1a3
Create Date: 2024-09-20 21:21:30.680127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06a82c13584e'
down_revision: Union[str, None] = 'cd8a2b91a1a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
