#!/usr/bin/python3
"""
This script update the name of
the State object with id = 2
to `New Mexico` in the database.
"""

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    """
    Updates a State object on the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    session.commit()
    session.close()
