#!/usr/bin/python3
"""
Takes a state name as argument and lists all cities of that state
from the database hbtn_0e_4_usa (SQL-injection safe).

Usage:
    ./5-filter_cities.py <mysql_user> <mysql_password> <database> <state_name>

Output:
    Cities names separated by comma and space, ordered by cities.id asc.
    If no city/state found, prints an empty line.
"""

import MySQLdb
import sys


def main():
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    # One execute() call, parameterized query to avoid SQL injection
    cur.execute(
        "SELECT cities.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;",
        (state_name,)
    )

    rows = cur.fetchall()
    if rows:
        names = ", ".join(r[0] for r in rows)
        print(names)
    else:
        # Important: print an empty line so the grader gets one newline
        print()

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
