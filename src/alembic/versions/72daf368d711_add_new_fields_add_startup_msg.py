"""add new fields add startup msg

Revision ID: 72daf368d711
Revises: bb6022ac747b
Create Date: 2023-12-29 00:01:38.615497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "72daf368d711"
down_revision: Union[str, None] = "bb6022ac747b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "datasets", sa.Column("startup_message_template", sa.String(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("datasets", "startup_message_template")
    # ### end Alembic commands ###
