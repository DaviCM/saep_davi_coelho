import enum

from sqlalchemy import Column, Integer, Numeric, String, Enum, Date
from sqlalchemy.orm import relationship

from database import Base

class Units(enum.Enum):
    kg = "kg"
    m2 = "m2"
    l = "l"
    qtd = "qtd"

    

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    description = Column(String(120), nullable=False)
    unit = Column(Enum(Units), nullable=False)
    quantity = Column(Numeric, nullable=False)
    expiration_date = Column(Date, nullable=False)

    logs = relationship("Log", back_populates="product")