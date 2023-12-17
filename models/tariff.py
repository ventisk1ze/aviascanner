from typing import List

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from .base import Base


class Tariff(Base):
    __tablename__ = 'tariff'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(5))
    name: Mapped[str] = mapped_column(String(20))
    usd_price: Mapped[float]

    reservations: Mapped[List['Reservation']] = relationship(back_populates='tariff')