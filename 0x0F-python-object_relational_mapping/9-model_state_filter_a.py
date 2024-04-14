#!/usr/bin/python3
"""lists all State objects that contain the letter a from hbtn_0e_6_usa db"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for state in session.query(State).\
            filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
