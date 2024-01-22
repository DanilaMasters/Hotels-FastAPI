from fastapi import APIRouter, Depends, Request
from hotels.bookings.dao import BookingDAO
from hotels.bookings.schemes import SBooking
from hotels.users.dependencies import get_current_user
from hotels.users.models import User

router = APIRouter(prefix='/bookings', tags=['Bookings'])


@router.get('/')
async def get_bookings(user: User = Depends(get_current_user)):
    return await BookingDAO.get_all_or_none(user_id=user.id)


@router.get('/{id}', response_model=SBooking)
async def get_bookings_id(id: int): 
    return await BookingDAO.get_by_id(model_id=id)

@router.post('/add')
async def add_booking(room_id, date_from, date_to, user: User = Depends(get_current_user)):
    return await BookingDAO.add(user.id, room_id, date_from, date_to)