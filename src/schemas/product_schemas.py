from typing import Literal, Optional
from decimal import Decimal
from datetime import date

from pydantic import BaseModel, ConfigDict


class CreateProductSchema(BaseModel):
    description: str
    unit: Literal["kg", "m2", "l", "qtd"]
    quantity: Decimal
    expiration_date: date



class QueryProductSchema(BaseModel):
    description: Optional[str] = None
    unit: Optional[Literal["kg", "m2", "l", "qtd"]] = None
    minimum_quantity: Optional[Decimal] = None
    maximum_quantity: Optional[Decimal] = None
    minimum_expiration_date: Optional[date] = None
    maximum_expiration_date: Optional[date] = None



class UpdateProductSchema(BaseModel):
    id: int
    quantity: Optional[Decimal] = None
    expiration_date: Optional[date] = None



class ResponseProductSchema(BaseModel):
    id: int
    description: str
    unit: Literal["kg", "m2", "l", "qtd"]
    quantity: Decimal
    expiration_date: date

    model_config = ConfigDict(
        from_attributes=True
    )

