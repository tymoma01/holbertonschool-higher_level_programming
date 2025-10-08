#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument (safe from SQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    # Parameterized query (MySQLdb uses %s placeholders)
    cur.execute(
        """SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC;""",
        (state_name,)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
