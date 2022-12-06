#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa database that matches the arg
while avoiding MySQL injections."""

import sys
import MySQLdb


if __name__ == "__main__":
    my_connect = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            host="localhost",
            port=3306
        )

    my_cursor = my_connect.cursor()
    sql = """SELECT * FROM states \
            WHERE  name = %s \
            ORDER BY id ASC"""

    my_cursor.execute(sql, (sys.argv[4],))
    result = my_cursor.fetchall()

    for i in result:
        print(i)
    my_connect.close()
