"""remove_column_name

Revision ID: c3c9d3293204
Revises: cabebb5e72e9
Create Date: 2024-07-04 02:25:27.532048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3c9d3293204'
down_revision: Union[str, None] = 'cabebb5e72e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('users', 'name')
    pass


def downgrade() -> None:
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
    pass
