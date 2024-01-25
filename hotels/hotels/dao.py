from datetime import date
from hotels.bookings.models import Booking
from hotels.hotels.models import Hotels
from hotels.dao.base import BaseDAO
from hotels.hotels.models import Hotels, Room
from hotels.database import async_session_maker
from sqlalchemy import and_, column, func, or_, select


class HotelDAO(BaseDAO):
    model = Hotels




    # @classmethod
    # async def get_all(cls, location: str, date_from: date, date_to: date):
    #     """
    #     select sum(rooms_left) from (with booked_rooms as (select * from bookings where
    #     (date_from >= '2025-06-15' and date_from <= '2025-06-20') or (date_from <= '2025-06-15' and date_to > '2025-06-15'))
    #     select (rooms.quantity - count(booked_rooms.id)) as rooms_left from rooms
    #     left join booked_rooms on booked_rooms.room_id = rooms.id where hotel_id = 1
    #     group by rooms.quantity)
    #     """
    #     pass
    #     # async with async_session_maker() as session:
    #     #     booked_rooms = select(Booking).where(
    #     #         or_(
    #     #             and_(
    #     #                 Booking.date_from >= date_from,
    #     #                 Booking.date_from <= date_to,
    #     #             ),
    #     #             and_(
    #     #                 Booking.date_from <= date_from,
    #     #                 Booking.date_to > date_from,    
    #     #             )    
    #     #         )
    #     #     ).cte('booked_rooms')

    #     #     get_rooms_left = select(
    #     #         (Room.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
    #     #     ).select_from(Room).join(
    #     #         booked_rooms, booked_rooms.c.room_id == Room.id, isouter=True
    #     #     ).where(Room.hotel_id == 2).group_by(
    #     #         Room.quantity
    #     #     )

    #     #     result = await session.execute(get_rooms_left)
    #     #     return sum(result.scalars().all())
