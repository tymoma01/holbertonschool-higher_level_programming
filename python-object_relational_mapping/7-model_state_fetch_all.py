#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Bind session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states ordered by id
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
