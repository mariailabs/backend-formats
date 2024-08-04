from sqlalchemy import Column, Integer, String
from models.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    name = Column(String(70))
    email = Column(String(50))
    hashed_password = Column(String(70))
    
class Taxi(Base):
    __tablename__ = 'taxi'

    id = Column(Integer, primary_key=True, autoincrement=True)
    town = Column(String(50))
    km = Column(String(50))
    time = Column(String(50))
    price = Column(String(50))


class Bus(Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    zone_id = Column(String(50))
    origin = Column(String(50))
    dispatch = Column(String(50))
    destination = Column(String(50))
    price = Column(String(50))

class Zone(Base):
    __tablename__ = 'zone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    zone = Column(String(50))



