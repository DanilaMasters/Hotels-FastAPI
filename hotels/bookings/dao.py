from hotels.bookings.models import Booking
from hotels.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Booking