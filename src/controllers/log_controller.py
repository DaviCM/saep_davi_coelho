from decimal import Decimal

from sqlalchemy import select

from models import Log
from schemas import QueryLogSchema
from database import Session
from errors import LogNotFoundError

def create_log(transaction_type: str, quantity: Decimal, product_id: int):
    new_log = Log(
        transction_type=transaction_type,
        quantity=quantity,
        product_id=product_id
    )

    with Session() as session:
        session.add(new_log)
        session.commit()


