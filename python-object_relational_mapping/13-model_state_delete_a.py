#!/usr/bin/python3
"""script that deletes all State objects with a
name containing the letter 'a' from the database hbtn_0e_6_usa."""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    my_engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=my_engine)
    my_session = Session()
    Base.metadata.create_all(my_engine)

    states = my_session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        my_session.delete(state)

    my_session.commit()

    my_session.close()
