from pydantic import BaseModel, EmailStr


class SUserRegistration(BaseModel):
    email: EmailStr
    password: str