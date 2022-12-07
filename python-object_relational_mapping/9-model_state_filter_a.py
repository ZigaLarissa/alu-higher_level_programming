#!/usr/bin/python3
"""A script that lists all states with letter a"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    my_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                    )
    Session = sessionmaker(bind=my_engine)

    Base.metadata.create_all(my_engine)

    my_session = Session()

    states = my_session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    my_session.close()
