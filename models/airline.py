from typing import List

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class Airline(Base):
    __tablename__ = 'airline'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    short_name: Mapped[str] = mapped_column(String(10))

    reservations: Mapped[List['Reservation']] = relationship(back_populates='airline')