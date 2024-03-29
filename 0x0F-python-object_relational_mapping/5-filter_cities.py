#!/usr/bin/python3
"""
script lists all cities in a given state
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    query = "SELECT cities.id, cities.name \
            FROM cities \
            JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))

    cur.close()
    db.close()
