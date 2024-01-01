"""create post table

Revision ID: 16e2636d06d0
Revises: 9f143bc7c85e
Create Date: 2023-12-31 09:26:40.001716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16e2636d06d0'
down_revision: Union[str, None] = '9f143bc7c85e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
