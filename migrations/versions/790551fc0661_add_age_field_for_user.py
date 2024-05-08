"""add age field for user

Revision ID: 790551fc0661
Revises: dcd5208fd19d
Create Date: 2024-05-08 16:15:13.519876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '790551fc0661'
down_revision: Union[str, None] = 'dcd5208fd19d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'age')
    # ### end Alembic commands ###
