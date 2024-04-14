#!/usr/bin/python3
"""prints the first State object from the database"""

if __name__ == "__main__":

    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)

    session = Session(eng)
    one = session.query(State).order_by(State.id).one()
    if one:
        print("{}: {}".format(one.id, one.name))
    else:
        print("Nothing")
    session.close()
