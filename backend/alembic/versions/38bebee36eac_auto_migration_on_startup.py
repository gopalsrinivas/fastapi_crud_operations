"""Auto migration on startup

Revision ID: 38bebee36eac
Revises: 6ee941cfee04
Create Date: 2024-09-20 21:21:07.414501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38bebee36eac'
down_revision: Union[str, None] = '6ee941cfee04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
