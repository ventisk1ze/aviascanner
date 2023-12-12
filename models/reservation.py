from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass


class Reservation(Base):
    __tablename__ = 'reservation'

    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='reservations')
    
    departure_airport_id: Mapped[int] = mapped_column(ForeignKey('airport.id'))
    departure_airport: Mapped['Airport'] = relationship(back_populates='departure_reservations')
    
    arrival_airport_id: Mapped[int] = mapped_column(ForeignKey('airport.id'))
    arrival_airport: Mapped['Airport'] = relationship(back_populates='arrival_reservations')
    
    airline_id: Mapped[int] = mapped_column(ForeignKey('airline.id'))
    airline: Mapped['Airline'] = relationship(back_populates='reservations')
    
    aircraft_type_id: Mapped[int] = mapped_column(ForeignKey('aircraft_type.id'))
    aircraft_type: Mapped['AircraftType'] = relationship(back_populates='reservations')
    
    tariff_id: Mapped[int] = mapped_column(ForeignKey('tariff.id'))
    tariff: Mapped['Tariff'] = relationship(back_populates='reservations')

    departure_time: Mapped[datetime] = mapped_column(DateTime())
    arrival_time: Mapped[datetime] = mapped_column(DateTime())
    