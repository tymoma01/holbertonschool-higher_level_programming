#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server on localhost, port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute the query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch and print all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
