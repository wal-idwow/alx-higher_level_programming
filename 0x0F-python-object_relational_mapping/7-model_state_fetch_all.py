#!/usr/bin/python3

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    for ins in sess.query(State).order_by(State.id):
        print(ins.id, ins.name, sep=": ")
