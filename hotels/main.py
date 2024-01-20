from datetime import date
from typing import Optional

from fastapi import Depends, Query
from pydantic import BaseModel
from hotels import app

from hotels.bookings.router import router as booking_router
from hotels.users.router import router as auth_router

app.include_router(auth_router)
app.include_router(booking_router)

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



@app.get('/hotels/')
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

@app.post('/booking')
def add_bookings():
    pass
