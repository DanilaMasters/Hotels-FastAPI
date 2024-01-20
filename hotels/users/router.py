from fastapi import APIRouter, HTTPException
from hotels.users.auth import get_password_hash
from hotels.users.dao import UserDAO

from hotels.users.scheme import SUserRegistration

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/register')
async def register(user_data: SUserRegistration):
    existing_user = await UserDAO.get_all_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(401)
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)

    