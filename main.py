import tkinter as tk
import mysql.connector
from mysql.connector import Error


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.queryAddIngr = ("INSERT INTO ingredients (ingr_group_id, calories, provider_id, ingredient_name) "
                             "VALUES (%s, %s, %s, %s)")
        self.queryAddRecipt = ("INSERT INTO recipt (recipt_id, recipt_name, descrption, author_id) "
                               "VALUE (%s. %s, %s, %s)")
        self.queryAddSupplier = ("INSERT INTO providers (provider_id, provider_name, address, phone)"
                                 "VALUE (%s, %s, %s, %s)")
        self.buttons = []
        self.rows = 0
        self.columns = 0
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.createbtn("Add ingredient", self.btn1Window)
        # self.createbtn("Edit ingredient", self.btn1)
        # self.createbtn("Delete ingredient", self.btn1)
        # self.createbtn("Add recipe", self.btn1)
        # self.createbtn("Edit recipe", self.btn1)
        # self.createbtn("Delete recipe", self.btn1)
        # self.createbtn("Add supplier", self.btn1)
        # self.createbtn("Edit supplier", self.btn1)
        # self.createbtn("Delete supplier", self.btn1)

        # quit
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=self.rows + 1, column=self.columns + 1, ipadx=10, ipady=6, padx=10, pady=10)

    def createbtn(self, text, command):
        self.newButtn = tk.Button(self)
        self.newButtn["text"] = text
        self.newButtn["command"] = command()
        self.newButtn.grid(row=self.rows, column=self.columns, ipadx=10, ipady=6, padx=10, pady=10)
        self.columns += 1
        if self.columns == 3:
            self.columns = 0
            self.rows += 1
        self.buttons.append(self.newButtn)

    # connect to kb
    def connect(self, state=True):
        try:
            conn = mysql.connector.connect(host='localhost', database='food', user='monstrillllo',
                                           password='123q123w123e')
            return conn
        except Error as e:
            print(e)

    # disconnect from kb
    def disconnect(self, conn):
        conn.close()

    # command for btn1
    def btn1Window (self):
        btn1Window = tk.Toplevel()
        btn1Window.title("Add ingredient")

    def addtokb(self, query):
        try:
            data = (1, 0.18, 4, "Orange")
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
        except Error as e:
            print(e)
        finally:
            conn.commit()
            cursor.close()
            self.disconnect(conn)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
