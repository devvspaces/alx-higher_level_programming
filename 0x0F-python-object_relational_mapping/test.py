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
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(
        City, State
    ).filter(City.state_id==State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
