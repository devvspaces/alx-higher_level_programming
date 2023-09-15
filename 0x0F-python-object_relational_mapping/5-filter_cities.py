#!/usr/bin/python3
"""Module to list all cities from database
hbtn_0e_0_usa filter by state name
free from MySQL injections
"""

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
        WHERE states.name=%s
        ORDER BY id ASC
        """,
        (sys.argv[4],)
    )
    rows = cur.fetchall()
    result = ""
    for row in rows:
        result += row[1] + ", "
    print(result[:-2])

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
