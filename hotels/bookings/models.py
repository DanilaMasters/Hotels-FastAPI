from sqlalchemy import Column, Computed, Date, ForeignKey, Integer
from hotels.database import Base


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed('(date_from - date_to) * price'))
    total_days = Column(Integer, Computed('date_from - date_to'))
