#!/usr/bin/python3
"""
This script prints all City objects
from the database.
"""

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))

    # Create all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # Create a configured "Session" class.
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State)

    for city, state in results.all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.commit()
    session.close()
