"""init-db

Revision ID: cabebb5e72e9
Revises: 
Create Date: 2024-07-04 00:22:12.171962

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cabebb5e72e9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
            CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
        """
    )
    op.execute(
        """
            CREATE TABLE users (
                id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
                name TEXT NOT NULL
            );
        """
    )
    op.execute(
        """
            CREATE TABLE urls (
                id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
                shorten TEXT NOT NULL,
                current TEXT NOT NULL,
                user_id uuid REFERENCES users(id) ON DELETE CASCADE,
                created_at timestamptz NOT NULL DEFAULT NOW()
                
            );
        """
    )
    pass


def downgrade() -> None:
    # SQL brut pour annuler la migration
    op.execute(
        """
            DROP TABLE urls;
            DROP TABLE users;
        """
    )
    pass
