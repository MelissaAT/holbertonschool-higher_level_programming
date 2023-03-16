#!/usr/bin/python3
"""Write a script that lists all State
objects from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    db = 'mysql+mysqldb://{}:{}@localhost/{}'

    engine = create_engine(db.format(username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    #new session instance
    session = Session()

    results = session.query(State).all()
    print(results)


    for states in results:
        idx = "{}:"
        print(idx.format(states.id), states.name)

    session.close()
