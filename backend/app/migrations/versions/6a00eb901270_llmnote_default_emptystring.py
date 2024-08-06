"""llmNote default emptystring

Revision ID: 6a00eb901270
Revises: 14163f1e4388
Create Date: 2024-08-06 06:18:23.158559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a00eb901270'
down_revision: Union[str, None] = '14163f1e4388'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
