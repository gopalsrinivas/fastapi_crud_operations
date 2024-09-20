"""Auto migration on startup

Revision ID: 00bd68450378
Revises: 327519b181a6
Create Date: 2024-09-20 21:20:20.280467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00bd68450378'
down_revision: Union[str, None] = '327519b181a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
