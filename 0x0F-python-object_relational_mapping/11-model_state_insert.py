#!/usr/bin/python3
"""
This script adds
the State object
`Louisiana` to the
database.
"""

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print('{0}'.format(new_state.id))
    session.close()
