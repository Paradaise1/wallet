import uuid

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Wallet(Base):
    '''Wallet model.'''
    __tablename__ = 'wallets'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    balance: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
