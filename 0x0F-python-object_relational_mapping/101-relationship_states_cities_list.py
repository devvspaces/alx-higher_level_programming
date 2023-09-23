#!/usr/bin/python3
"""
Lists all State objects and corresponding
City objects contained in the DB
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State

if __name__ == '__main__':
    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # Create a configured "Session" class.
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(
        City).order_by(State.id, City.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
