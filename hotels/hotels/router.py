from datetime import date
import time
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from hotels.hotels.dao import HotelDAO


router = APIRouter(prefix='/hotels', tags=['Hotel manager'])


@router.get('')
@cache(expire=60)
async def hotels():
    time.sleep(3)
    return await HotelDAO.get_all()

@router.get('/{location}')
@cache(expire=60)
async def hotels_list(location: str, date_from: date, date_to: date):
    return await HotelDAO.get_all(location=location, date_from=date_from, date_to=date_to)

