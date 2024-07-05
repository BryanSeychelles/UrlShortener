"""create_foreignkey_table

Revision ID: 77acd5baa761
Revises: c3c9d3293204
Create Date: 2024-07-04 14:42:12.783969

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "77acd5baa761"
down_revision: Union[str, None] = "c3c9d3293204"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
            CREATE TABLE search_by_user (
                id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
                user_id uuid REFERENCES users(id) ON DELETE CASCADE,
                url_id uuid REFERENCES urls(id) ON DELETE CASCADE
            );
        """
    )
    op.execute(
        """
            INSERT INTO search_by_user (user_id, url_id)
            SELECT user_id, id FROM urls;
        """
    )
    op.execute(
        """
            ALTER TABLE urls DROP COLUMN user_id;
        """
    )
    pass


def downgrade() -> None:
    op.execute(
        """
            ALTER TABLE urls ADD COLUMN user_id uuid REFERENCES users(id) ON DELETE CASCADE;
        """
    )
    op.execute(
        """
            INSERT INTO urls (user_id)
            SELECT user_id FROM search_by_user;
        """
    )
    op.execute(
        """
            DROP TABLE search_by_user;
        """
    )
    pass
