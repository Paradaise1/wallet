"""Initial

Revision ID: 5da9d5a20221
Revises: 
Create Date: 2024-11-02 19:45:59.563989

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5da9d5a20221'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wallets',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('balance', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallets')
    # ### end Alembic commands ###