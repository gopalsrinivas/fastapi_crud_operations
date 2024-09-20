"""Auto migration on startup

Revision ID: b769b739a39d
Revises: 06a82c13584e
Create Date: 2024-09-20 21:21:36.314888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b769b739a39d'
down_revision: Union[str, None] = '06a82c13584e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
