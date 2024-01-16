"""add new fields add ts

Revision ID: 7c5b69666f6d
Revises: 2d466596de91
Create Date: 2023-12-27 12:34:32.310467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7c5b69666f6d"
down_revision: Union[str, None] = "2d466596de91"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("simulation_profiles", sa.Column("ts", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("simulation_profiles", "ts")
    # ### end Alembic commands ###
