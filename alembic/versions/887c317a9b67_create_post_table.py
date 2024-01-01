"""create post table

Revision ID: 887c317a9b67
Revises: 
Create Date: 2023-12-29 23:36:26.866095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '887c317a9b67'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('user_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('userid', sa.String(), nullable=False),
        sa.Column('pas', sa.String(), nullable=False)
    )
    pass

def downgrade():
    op.drop_table('posts')
    pass