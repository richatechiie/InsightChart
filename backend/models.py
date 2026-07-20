from sqlalchemy import Column, Integer, Float, String
from database import Base

class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True, index=True)

    passenger_id = Column(Integer)
    survived = Column(Integer)
    pclass = Column(Integer)
    name = Column(String)
    sex = Column(String)
    age = Column(Float)
    sibsp = Column(Integer)
    parch = Column(Integer)
    ticket = Column(String)
    fare = Column(Float)
    cabin = Column(String)
    embarked = Column(String)