from typing import Optional

from sqlalchemy import select

from models import Product
from schemas import CreateProductSchema, QueryProductSchema, UpdateProductSchema
from database import Session
from controllers import create_log
from errors import ProductNotFoundError, InvalidQuantityError, InvalidDateError

def get_product_by_id(id: int) -> Optional[Product]:
    stmt = select(Product).where(Product.id == id)
    
    with Session() as session:
        target_product = session.scalar(stmt)

    return target_product if target_product != None else None


def create_product(params: CreateProductSchema) -> Product:
    if params.quantity < 0:
        raise InvalidQuantityError

    new_product = Product(
        description=params.description,
        unit=params.unit,
        quantity=params.quantity,
        expiration_date=params.expiration_date
    )

    with Session() as session:
        session.add(new_product)
        session.commit()

    return new_product


def list_products(params: QueryProductSchema) -> list[Product]:
    if (params.minimum_quantity != None) and (params.maximum_quantity != None):
        if params.minimum_quantity > params.maximum_quantity:
            raise InvalidQuantityError

    if (params.minimum_expiration_date != None) and (params.maximum_expiration_date != None):
            if params.minimum_expiration_date > params.maximum_expiration_date:
                raise InvalidDateError

    stmt = select(Product)

    if params.description != None:
        stmt = stmt.where(params.description in Product.description)

    if params.unit != None:
        stmt = stmt.where(Product.unit == params.unit)

    if params.minimum_quantity != None:
        stmt = stmt.where(Product.quantity >= params.minimum_quantity)

    if params.maximum_quantity != None:
        stmt = stmt.where(Product.quantity <= params.maximum_quantity)

    if params.minimum_expiration_date != None:
        stmt = stmt.where(Product.expiration_date >= params.minimum_expiration_date)
    
    if params.maximum_expiration_date != None:
        stmt = stmt.where(Product.expiration_date <= params.maximum_expiration_date)

    with Session() as session:
        products = session.scalars(stmt).all()

    if products == []:
        raise ProductNotFoundError
    else:
        return products


def update_product(params: UpdateProductSchema):
    if (params.quantity != None) and (params.quantity < 0):
        raise InvalidQuantityError

    target_product = get_product_by_id(params.id)

    if target_product == None:
        raise ProductNotFoundError

    current_quantity = target_product.quantity
    current_expiration = target_product.expiration_date

    with Session():
        if params.quantity != None:
            target_product.quantity = params.quantity

        if params.expiration_date != None:
            target_product.expiration_date = params.expiration_date

    transaction_type = "entry" if current_quantity < params.quantity else "exit"

    if current_quantity > params.quantity:
        logged_quantity = current_quantity - params.quantity
    else:
        logged_quantity = params.quantity - current_quantity

    create_log(transaction_type=transaction_type, quantity=logged_quantity, product_id=target_product.id)

    return target_product

