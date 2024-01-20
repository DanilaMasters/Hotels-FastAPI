from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from hotels.database import Base


class Hotels(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON, nullable=True)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, nullable=False)
    hotel_id = Column(ForeignKey('hotels.id'), nullable=False)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
