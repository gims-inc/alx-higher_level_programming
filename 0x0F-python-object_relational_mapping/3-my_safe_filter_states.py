#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Safe from SQL injections.
Usage: ./3-my_safe_filter_states.py <mysql username> \
                            <mysql password> \
                             <database name> \
                             <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
              (sys.argv[4],))
    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()
