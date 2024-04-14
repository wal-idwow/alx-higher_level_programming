#!/usr/bin/python3
"""value match given argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    DB = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = DB.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(sys.argv[4]))
    rws = cur.fetchall()
    for rw in rws:
        print(rw)
