#!/usr/bin/python3
"""Lists all cities in a state from hbtn_0e_4_usa database."""

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

    sql = """SELECT cities.name FROM states \
            INNER JOIN cities ON states.id = cities.state_id \
            WHERE states.name = %s ORDER BY cities.id ASC"""

    state = sys.argv[4]

    my_cursor.execute(sql, (state,))

    result = my_cursor.fetchall()

    print(", ".join([city[0] for city in result]))
    my_connect.close()
