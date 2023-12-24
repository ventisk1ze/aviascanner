from datetime import datetime


from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Flight(Base):
    __tablename__ = 'flights'

    id: Mapped[int] = mapped_column(primary_key=True)
    
    
    departure_airport_id: Mapped[int] = mapped_column(ForeignKey('airport.id'))
    departure_airport: Mapped['Airport'] = relationship(back_populates='departure_reservations')
    
    arrival_airport_id: Mapped[int] = mapped_column(ForeignKey('airport.id'))
    arrival_airport: Mapped['Airport'] = relationship(back_populates='arrival_reservations')
    
    airline_id: Mapped[int] = mapped_column(ForeignKey('airline.id'))
    airline: Mapped['Airline'] = relationship(back_populates='flights')
    
    aircraft_type_id: Mapped[int] = mapped_column(ForeignKey('aircraft_type.id'))
    aircraft_type: Mapped['AircraftType'] = relationship(back_populates='flights')
    
    tariff_id: Mapped[int] = mapped_column(ForeignKey('tariff.id'))
    tariff: Mapped['Tariff'] = relationship(back_populates='flights')

    departure_time: Mapped[datetime] = mapped_column(DateTime())
    arrival_time: Mapped[datetime] = mapped_column(DateTime())
    