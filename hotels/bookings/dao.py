from hotels.bookings.models import Booking
from hotels.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Booking

    @classmethod
    def add(cls, room_id, date_from, date_to):
        pass
