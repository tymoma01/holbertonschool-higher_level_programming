#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """List all State objects containing 'a' in their name."""
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]

    # Create engine (connect to MySQL server on localhost:3306)
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: filter states that contain 'a' (case-sensitive)
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()


if __name__ == "__main__":
    main()
