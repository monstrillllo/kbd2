import mysql.connector
from mysql.connector import Error
from NewListBox import *
from TopLevelWindow import *


class connection():
    def __init__(self, query, val):
        self.conn = None
        self.cursor = None
        self.query = query
        self.val = val

    def connect(self):
        try:
            conn = mysql.connector.connect(host='localhost', database='food', user='monstrillllo',
                                           password='123q123w123e')
            return conn
        except Error as e:
            print(e)

    def addtokb(self):
        try:
            self.conn = self.connect()
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.query, self.val)
        except Error as e:
            print(e)
        finally:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def selectfromkb(self):
        try:
            self.conn = self.connect()
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.query, self.val)
            res = self.cursor.fetchall()
            return res
            #SelectWindow = TopLevelWindow(master, True, "Selected")
            #List = Listbox(master=SelectWindow)
            #for (date, supplier_id, supplier_name, address, phone, ingredient_name, ingr_price) in res:
            #    List.insert(END, date, supplier_id, supplier_name, address, phone, ingredient_name,
            #                ingr_price, "------")
            #List.pack()

        except Error as e:
            print(e)

        finally:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
