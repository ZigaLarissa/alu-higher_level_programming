#!/usr/bin/python3
"""Lists all states that starts with N."""

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
    my_cursor.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    result = my_cursor.fetchall()

    for i in result:
        print(i)
    my_connect.close()
