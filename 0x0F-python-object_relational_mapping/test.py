#!/usr/bin/python3
"""
Select all states
that contains an 'a' in the name from supplied db
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from model_state import Base, State, Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
#     state = relationship('State', back_populates='cities')


# State.cities = relationship('City', order_by=City.id, back_populates='state')

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.Que

    session.commit()
    session.close()
