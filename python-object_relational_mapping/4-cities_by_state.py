#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cur = db.cursor()

    # Execute query only once
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities INNER JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
