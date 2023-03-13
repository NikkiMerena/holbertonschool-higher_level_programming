#!/usr/bin/python3
"""
This python script lists all states from hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Section to remove rows that contain 'a'
    for row in session.query(State).filter(State.name.contains("a")):
        session.delete(row)

    session.commit()
