import mysql.connector
from mysql.connector import Error


def connect():
    try:
        conn = mysql.connector.connect(host='localhost', database='food', user='monstrillllo',
                                           password='123q123w123e')
        return conn
    except Error as e:
        print(e)

def disconnect(conn):
    conn.close()

def addtokb(query, val):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, val)
    except Error as e:
        print(e)
    finally:
        conn.commit()
        cursor.close()
        conn.close()
