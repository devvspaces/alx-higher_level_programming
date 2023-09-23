#!/usr/bin/python3
"""
Select all states
that contains an 'a' in the name from supplied db
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, selectinload, joinedload, subqueryload

from relationship_city import Base, State, City


if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State)\
        .outerjoin(City)\
        .options(selectinload(State.cities))\
        .order_by(City.id)\
            .all():
        print("{}: {}".format(state.id, state.name))
        if len(State.cities) != 0:
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))

    session.close()
