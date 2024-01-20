from datetime import date
from pydantic import BaseModel, Field


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        orm_mode = True

class SBookingResponse(BaseModel):
    Booking: SBooking = Field()