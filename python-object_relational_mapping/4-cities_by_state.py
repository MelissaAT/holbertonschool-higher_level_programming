#!/usr/bin/python3
"""Write a script that lists all cities from the
database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
        )
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states\
        ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    
    rows = cursor.fetchal()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()