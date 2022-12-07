#!/usr/bin/python3
"""Prints the first state objects from the database hbtn_0e_6_usa."""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    my_engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(my_engine)

    my_session = Session(my_engine)

    state = my_session.query(State).first()

    if state:
        print("{}: {}".format(state.__dict__["id"], state.__dict__["name"]))
    else:
        print("Nothing")

    my_session.close()
