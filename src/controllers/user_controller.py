from typing import Optional

from sqlalchemy import select
from argon2 import PasswordHasher

from models import User
from schemas import CreateUserSchema, LoginUserSchema, ResponseUserSchema
from errors import UserAlreadyExistsError, UserNotFoundError, WrongUserInfoError
from database import Session

argon2 = PasswordHasher()

def verify_password(hashed: str, password: str) -> bool:
    try:
        argon2.verify(hash=hashed, password=password)
        return True
    
    except Exception:
        return False


def get_user_by_email(email: str) -> Optional[User]:
    stmt = select(User).where(User.email == email)
    
    with Session() as session:
        target_user = session.scalar(stmt)

    return target_user if target_user != None else None
        

def create_user(params: CreateUserSchema) -> User:
    if get_user_by_email(params.email) != None:
        raise UserAlreadyExistsError

    password = argon2.hash(params.password.get_secret_value())

    new_user = User(
        name=params.name,
        email=params.email,
        password=password
    )

    with Session() as session:
        session.add(new_user)
        session.commit()

    return new_user


def login(params: LoginUserSchema) -> User:
    target_user = get_user_by_email(params.email)

    if target_user == None:
        raise UserNotFoundError

    if verify_password(target_user.password, params.password) == False:
        raise WrongUserInfoError
    else:
        return target_user


    
    