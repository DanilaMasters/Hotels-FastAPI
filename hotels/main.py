from datetime import date
from typing import Optional

from fastapi import Depends, Query
from pydantic import BaseModel
from hotels import app


class HotelsSearchArgs():
    def __init__(self,
        location: str,
        date_from:date ,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(title="Number if stars", ge=1, le=5)          
    ):
        self.location = location;
        self.date_from = date_from;
        self.date_to = date_to;
        self.has_spa = has_spa;
        self.stars = stars;


class SHotel(BaseModel):
    name: str
    address: str
    stars: int

@app.get('/hotels/', response_model=SHotel)
def index(
        search_args: HotelsSearchArgs = Depends()
    ):

    hotels = [
        {
            'name': 'Hotel',
            'address': 'Address',
            'stars': 5
        }
    ]

    return hotels[0]

class SBooking(BaseModel):
    room_id: int
    date_from: str
    date_to: str

@app.post('/booking')
def add_bookings(booking: SBooking):
    pass
