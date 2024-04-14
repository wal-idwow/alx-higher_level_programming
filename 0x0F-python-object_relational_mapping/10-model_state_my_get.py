#!/usr/bin/python3
"""Prints the State object with the name passed
as an argument from hbtn_0e_6_usa db"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm.exc import NoResultFound
    from model_state import Base, State

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(eng)

    Session = sessionmaker(bind=eng)
    session = Session()

    try:
        state = session.query(State).filter(State.name == sys.argv[4]).one()
        print("{}".format(state.id))
    except NoResultFound:
        print("Not found")

    session.close()
