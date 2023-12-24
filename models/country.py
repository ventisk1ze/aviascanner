from typing import List


from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from .base import Base


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    continent: Mapped[str] = mapped_column(String(20))
    currencty: Mapped[str] = mapped_column(String(3))

    airports: Mapped[List['Airport']] = relationship(back_populates='country')