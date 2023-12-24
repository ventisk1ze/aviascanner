from typing import List


from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, ForeignKey
from .base import Base


class Airport(Base):
    __tablename__ = 'airport'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    iata_short: Mapped[str] = mapped_column(String(5))
    icao_short: Mapped[str] = mapped_column(String(5))
    timezone: Mapped[str] = mapped_column(String(5))

    country_id: Mapped[int] = mapped_column(ForeignKey('country.id'))
    country: Mapped['Country'] = relationship(back_populates='airports')

    departure_reservations: Mapped[List["Flight"]] = relationship(back_populates='departure_airport')
    arrival_reservations: Mapped[List["Flight"]] = relationship(back_populates='arrival_airport')