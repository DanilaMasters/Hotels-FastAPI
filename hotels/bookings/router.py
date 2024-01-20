from fastapi import APIRouter
from hotels.bookings.dao import BookingDAO
from hotels.bookings.schemes import SBooking

router = APIRouter(prefix='/bookings', tags=['Bookings'])


@router.get('/', response_model=list[SBooking])
async def get_bookings():
    return await BookingDAO.get_all()

@router.get('/{id}', response_model=SBooking)
async def get_bookings_id(id: int): 
    return await BookingDAO.get_by_id(model_id=id)

