from typing import Literal, Optional
from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, ConfigDict

class QueryLogSchema(BaseModel):
    id: Optional[int] = None
    datetime: Optional[datetime] = None
    transaction_type: Optional[Literal["entry", "exit"]] = None
    quantity: Optional[Decimal] = None
    product_id: Optional[int] = None



class ResponseLogSchema(BaseModel):
    id: int
    datetime: datetime
    transaction_type: Literal["entry", "exit"]
    quantity: Decimal
    product_id: int

    model_config = ConfigDict(
        from_attributes=True
    )
