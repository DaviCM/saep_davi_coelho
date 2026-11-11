from pydantic import BaseModel, ConfigDict, EmailStr, SecretStr

class CreateUserSchema(BaseModel):
    name: str
    email = EmailStr
    password = SecretStr



class LoginUserSchema(BaseModel):
    email = EmailStr
    password = SecretStr



class ResponseUserSchema:
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True
    )

