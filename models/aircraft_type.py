from typing import List

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from .base import Base


class AircraftType(Base):
    __tablename__ = 'aircraft_type'

    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturer: Mapped[str] = mapped_column(String(20))
    model: Mapped[str] = mapped_column(String(20))
    effectiveRange: Mapped[float]
    cruisingSpeed: Mapped[float]
    capacity: Mapped[int]

    reservations: Mapped[List['Reservation']] = relationship(back_populates='aircraft_type')