#!/usr/bin/python3
"""Module to list all states from database
hbtn_0e_0_usa filter with user input"""

import sys

import MySQLdb


def main():
    """Function main"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
