import mysql.connector
from mysql.connector import Error


class connection():
    def __init__(self, query, val):
        self.conn = None
        self.cursor = None
        self.query = query
        self.val = val
        self.addtokb(self.query, self.val)

    def connect(self):
        try:
            conn = mysql.connector.connect(host='localhost', database='food', user='monstrillllo',
                                           password='123q123w123e')
            return conn
        except Error as e:
            print(e)

    def addtokb(self, query, val):
        try:
            self.conn = self.connect()
            self.cursor = self.conn.cursor()
            print(val)
            self.cursor.execute(query, val)
        except Error as e:
            print(e)
        finally:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
