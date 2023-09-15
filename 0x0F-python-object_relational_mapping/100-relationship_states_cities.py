#!/usr/bin/python3
"""
Creates the State "California"
with the City "San Francisco" from the database
"""

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    # Create all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # Create a configured "Session" class.
    Session = sessionmaker(bind=engine)
    session = Session()

    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    # Add the new objects to the session.
    session.add(cal_state)
    session.commit()
    session.close()
