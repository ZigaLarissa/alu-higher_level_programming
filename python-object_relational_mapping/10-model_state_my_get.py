#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    my_engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(my_engine)
    my_session = Session(my_engine)

    state_name = sys.argv[4]

    state = my_session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(f'{state.id}')

    my_session.close()
