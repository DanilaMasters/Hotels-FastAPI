from fastapi import APIRouter
from hotels.bookings.dao import BookingDAO
from hotels.dao.base import BaseDAO

router = APIRouter(prefix='/bookings', tags=['Bookings'])


@router.get('/')
async def get_bookings():
    result = await BookingDAO.get_all()
    return result
