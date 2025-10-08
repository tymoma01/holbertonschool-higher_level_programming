#!/usr/bin/python3
"""
Script to get all states from the database hbtn_0e_0_usa
with names starting with 'N' (uppercase only).

Arguments:
    mysql username
    mysql password
    database name

Sorted by:
    ASC states.id
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Recover arguments from user
    user = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host='localhost',
        user=user,
        passwd=pswd,
        db=db_name,
        port=3306
    )

    # Create cursor
    cur = db.cursor()

    # Execute MySQL query
    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC;"
    )

    # Display results
    for row in cur.fetchall():
        print(row)

    # Close connections
    cur.close()
    db.close()
