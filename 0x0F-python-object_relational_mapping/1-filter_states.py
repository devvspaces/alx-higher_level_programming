#!/usr/bin/python3
"""Module to list all states from
database where name starts with N"""

import sys

import MySQLdb


def create_connection(user, password, db_name):
    """Function to create a connection with mysql"""
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=db_name)
    return db


def create_cursor(db):
    """Function to create a cursor"""
    cur = db.cursor()
    return cur


def print_states(cur):
    """Function to print states"""
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if (row[1][0] == 'N'):
            print(row)


def main():
    """Function main"""
    db = create_connection(sys.argv[1], sys.argv[2], sys.argv[3])
    cur = create_cursor(db)
    print_states(cur)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
