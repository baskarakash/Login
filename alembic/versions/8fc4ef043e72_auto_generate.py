"""auto generate

Revision ID: 8fc4ef043e72
Revises: 887c317a9b67
Create Date: 2023-12-31 09:08:31.200984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fc4ef043e72'
down_revision: Union[str, None] = '887c317a9b67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop the 'posts' table
    op.drop_table('posts')

    # Alter the 'employee' table columns
    op.alter_column('employee', 'empid',
                    existing_type=sa.INTEGER(),
                    nullable=False,
                    server_default=sa.text("nextval('employee_empid_seq'::regclass)"))  # Add server_default for auto-increment

    op.alter_column('employee', 'empname',
                    existing_type=sa.VARCHAR(),
                    nullable=True)

    # Create indexes on 'employee' table
    op.create_index(op.f('ix_employee_empid'), 'employee', ['empid'], unique=False)
    op.create_index(op.f('ix_employee_empname'), 'employee', ['empname'], unique=False)

    # Drop the foreign key constraint on 'employee' table
    op.drop_constraint('employee_empid_fkey', 'employee', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade() -> None:
    # Reverse the changes made in the 'upgrade' function

    # Create the foreign key constraint on 'employee' table
    op.create_foreign_key('employee_empid_fkey', 'employee', 'auth', ['empid'], ['user_id'])

    # Drop indexes on 'employee' table
    op.drop_index(op.f('ix_employee_empname'), table_name='employee')
    op.drop_index(op.f('ix_employee_empid'), table_name='employee')

    # Alter the 'employee' table columns back to the previous state
    op.alter_column('employee', 'empname',
                    existing_type=sa.VARCHAR(),
                    nullable=False)

    op.alter_column('employee', 'empid',
                    existing_type=sa.INTEGER(),
                    nullable=True,
                    autoincrement=True)  # Restore autoincrement parameter

    # Recreate the 'posts' table
    op.create_table('posts',
                    sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('userid', sa.VARCHAR(), nullable=False),
                    sa.Column('pas', sa.VARCHAR(), nullable=False),
                    sa.PrimaryKeyConstraint('user_id', name='posts_pkey')
                    )

    # ### end Alembic commands ###
