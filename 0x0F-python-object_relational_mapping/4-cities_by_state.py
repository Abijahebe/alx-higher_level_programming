#!/usr/bin/python3
"""
script lists all 'cities' from the given database
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
            From cities \
            JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
