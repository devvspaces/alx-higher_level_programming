#!/usr/bin/python3
"""
Select all states
that contains an 'a' in the name from supplied db
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # state = State(name="Louisiana")
    # session.add(state)

    # session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})

    session.commit()
    session.close()
