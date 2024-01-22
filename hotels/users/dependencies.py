from datetime import datetime
from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt
from exceptions import CurrentUserIdErrorException, JWTErrorMyException, NoSuchUserException, NoTokenException, TokenExpiredException
from hotels.users.dao import UserDAO

from hotels.config import ALGORITHM, SECRET_KEY

def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise NoTokenException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except JWTError:
        raise JWTErrorMyException
    expire: str = payload.get('exp')
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise TokenExpiredException
    user_id: str = payload.get('sub')
    if not user_id:
        raise CurrentUserIdErrorException
    user = await UserDAO.get_one_or_none(id=int(user_id))
    if not user:
        raise NoSuchUserException
    return user