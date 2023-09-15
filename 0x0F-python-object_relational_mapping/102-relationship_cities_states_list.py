#!/usr/bin/python3
"""
Lists all City objects
from the database in this format:
<city id>: <city name> -> <state name>
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

    states = session.query(State).join(City).order_by(City.id).all()
    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
