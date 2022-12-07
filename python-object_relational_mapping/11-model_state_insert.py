#!/usr/bin/python3
"""script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa."""

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

    state = State(name="Louisiana")
    my_session.add(state)
    my_session.commit()
    print(state.id)
    my_session.close()
