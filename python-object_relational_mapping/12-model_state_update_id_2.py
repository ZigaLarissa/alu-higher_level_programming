#!/usr/bin/python3
"""script that changes the name of a State object
from the database hbtn_0e_6_usa."""

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

    state = my_session.query(State).filter(State.id == 2).first()

    state.name = "New Mexico"

    my_session.commit()
    my_session.close()
