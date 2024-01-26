from datetime import date
from fastapi import APIRouter, Depends, Request
from pydantic import parse_obj_as
from exceptions import RoomCannotBeBookedException
from hotels.bookings.dao import BookingDAO
from hotels.bookings.schemes import SBooking
from hotels.tasks.tasks import send_booking_confirmation_email
from hotels.users.dependencies import get_current_user
from hotels.users.models import User
from pydantic import TypeAdapter

router = APIRouter(prefix='/bookings', tags=['Bookings'])


@router.get('/')
async def get_bookings(user: User = Depends(get_current_user)):
    return await BookingDAO.get_all_or_none(user_id=user.id)


@router.get('/{id}', response_model=SBooking)
async def get_bookings_id(id: int): 
    return await BookingDAO.get_by_id(model_id=id)

@router.post('/add')
async def add_booking(room_id: int, date_from: date, date_to: date, user: User = Depends(get_current_user)):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBookedException
    booking_dict = parse_obj_as(SBooking, booking).dict()
    send_booking_confirmation_email.delay(booking_dict, user.email)
    return booking_dict