from typing import List


from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from .base import Base

class Airline(Base):
    __tablename__ = 'airline'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    short_name: Mapped[str] = mapped_column(String(10))

    flights: Mapped[List['Flight']] = relationship(back_populates='airline')