#!/usr/bin/python3
"""Module to list all cities from database
hbtn_0e_0_usa"""

import sys

import MySQLdb


def main():
    """Function main"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY id ASC
        """
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
