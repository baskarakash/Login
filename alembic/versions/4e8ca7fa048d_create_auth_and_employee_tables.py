"""create_auth_and_employee_tables

Revision ID: 4e8ca7fa048d
Revises: 
Create Date: 2023-12-15 10:51:45.371844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e8ca7fa048d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        '''
        CREATE TABLE IF NOT EXISTS auth (
            user_id SERIAL NOT NULL,
            userid VARCHAR(256),
            pas VARCHAR(256),
            PRIMARY KEY (user_id)
        )
        '''
    )

    op.execute(
        '''
        CREATE TABLE IF NOT EXISTS employee (
            empid SERIAL NOT NULL,
            empname VARCHAR(256),
            empage VARCHAR(256),
            empsalary VARCHAR(256),
            PRIMARY KEY (empid)
        )
        '''
    )

# Define the downgrade function
def downgrade():
   ''' op.drop_table('auth')
    op.drop_table('employee')'''