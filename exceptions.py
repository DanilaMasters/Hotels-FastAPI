from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status

class BookingException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self, status_code: int, detail: Any = None) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BaseException):
    status_code = 401
    detail = 'User already exists'


class WrongUsernameOrPasswordException(BaseException):
    status_code = 401
    detail = 'Wrong username or password'


class NoTokenException(BaseException):
    status_code = 401
    detail = 'No token available'


class JWTErrorMyException(BaseException):
    status_code = 401
    detail = 'JWT Error'


class TokenExpiredException(BaseException):
    status_code = 401
    detail = 'Token expired'


class CurrentUserIdErrorException(BaseException):
    status_code = 401
    detail = 'Current user id error'


class NoSuchUserException(BaseException):
    status_code = 401
    detail = 'No such user'
