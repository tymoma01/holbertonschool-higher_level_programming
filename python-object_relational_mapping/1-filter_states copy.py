#!/usr/bin/python3
"""Lists all states starting with uppercase N."""
import MySQLdb, sys

if __name__ == "__main__":
    usr, pwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=usr, passwd=pwd, db=dbname)
    cur = db.cursor()

    # Force case-sensitive match: only names beginning with uppercase 'N'
    cur.execute("SELECT * FROM states WHERE name REGEXP BINARY '^N' ORDER BY id ASC;")

    for row in cur.fetchall():
        print(row)

    cur.close(); db.close()