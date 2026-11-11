import enum

from sqlalchemy import Column, Integer, Numeric, Enum, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from database import Base

class TransactionTypes(enum.Enum):
    entry = "entry"
    exit = "exit"



class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, server_default=func.now())
    transaction_type = Column(Enum(TransactionTypes), nullable=False)
    quantity = Column(Numeric, nullable=False)

    product_id = Column(ForeignKey("products.id", ondelete="cascade"))
    product = relationship("Product", back_populates="logs")