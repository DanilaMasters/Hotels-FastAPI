from datetime import date
from sqlalchemy import DATE, INTEGER, cast, func, insert, select, and_, or_
from hotels.bookings.models import Booking
from hotels.dao.base import BaseDAO
from hotels.hotels.models import Room
from hotels.database import engine, async_session_maker


class BookingDAO(BaseDAO):
    model = Booking

    @classmethod
    async def add(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        """
        with booked_rooms as (select * from bookings where room_id = 1 and (date_from >= '2023-05-15' and date_from <= '2023-06-20')
					 or (date_from <= '2023-05-15' and date_to > '2023-05-15'))
					 select rooms.quantity - count(booked_rooms.id) from rooms
					 left join booked_rooms on booked_rooms.room_id = rooms.id
					 where rooms.id = 1
					 group by rooms.quantity
        """
        async with async_session_maker() as session:
            booked_rooms = select(Booking).where(
                and_(
                    Booking.room_id == room_id,
                    or_(
                        and_(
                            Booking.date_from >= date_from,
                            Booking.date_from <= date_to
                        ),
                        and_(
                            Booking.date_from <= date_from,
                            Booking.date_to > date_from
                        )
                    )
                )
            ).cte('booked_rooms')

            get_rooms_left = select(
                (Room.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
            ).select_from(Room).join(
                booked_rooms, booked_rooms.c.room_id == Room.id, isouter=True
            ).where(Room.id == room_id).group_by(
                Room.quantity, booked_rooms.c.room_id
            )

            rooms_left = await session.execute(get_rooms_left)
            if rooms_left.scalar() > 0:
                price_query = select(Room.price).filter_by(id=room_id)
                price = await session.execute(price_query)
                price = price.scalar()
                add_booking_query = insert(Booking).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price,
                ).returning(Booking)
                
                new_booking = await session.execute(add_booking_query) 
                await session.commit()
                return new_booking.scalar()
            else:
                return None