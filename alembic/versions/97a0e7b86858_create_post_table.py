"""create post table

Revision ID: 97a0e7b86858
Revises: 16e2636d06d0
Create Date: 2023-12-31 10:42:57.916619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97a0e7b86858'
down_revision: Union[str, None] = '16e2636d06d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
