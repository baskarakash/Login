"""create post table

Revision ID: 9f143bc7c85e
Revises: 8fc4ef043e72
Create Date: 2023-12-31 09:18:17.157620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f143bc7c85e'
down_revision: Union[str, None] = '8fc4ef043e72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
