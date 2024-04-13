#!/usr/bin/python3
"""states starting with N lists from hbtn_0e_0_usa db"""

import MySQLdb
import sys

if __name__ == "__main__":
    DB = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = DB.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC;""")
    rws = cur.fetchall()
    for rw in rws:
        print(rw)
