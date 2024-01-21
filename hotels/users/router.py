from fastapi import APIRouter, Depends, HTTPException, Response
from hotels.users.auth import create_access_token, get_password_hash, verify_password
from hotels.users.dao import UserDAO
from hotels.users.dependencies import get_current_user
from hotels.users.models import User

from hotels.users.scheme import SUserAuth

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/register')
async def register(user_data: SUserAuth):
    existing_user = await UserDAO.get_all_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(401)
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post('/login')
async def login(response: Response, user_data: SUserAuth):
    user = await UserDAO.get_one_or_none(email=user_data.email)
    if not user or not verify_password(password=user_data.password, hashed_password=user.hashed_password):
        return HTTPException(401)
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('booking_access_token', value=access_token, httponly=True)
    return access_token
    

@router.post('/logout')
async def logout(response: Response):
    response.delete_cookie('booking_access_token')


@router.get('/me')
async def read_user(user: User = Depends(get_current_user)):
    return user