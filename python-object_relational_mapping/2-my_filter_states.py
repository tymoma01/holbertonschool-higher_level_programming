#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Get MySQL credentials and arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cur = db.cursor()

    # Use format to insert the argument directly (as required by the task)
    query = """SELECT * FROM states
            WHERE BINARY name = '{}'
            ORDER BY id ASC
            ;""".format(state_name)
    cur.execute(query)

    # Fetch and display results
    for row in cur.fetchall():
        print(row)

    # Close connections
    cur.close()
    db.close()
