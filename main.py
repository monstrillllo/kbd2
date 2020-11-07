import tkinter as tk
import mysql.connector
from mysql.connector import Error


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.buttons = []
        self.rows = 0
        self.columns = 0
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.createbtn(self, "Add ingredient", self.btn1Window)
        self.createbtn(self, "Edit ingredient", self.btn1Window)
        self.createbtn(self, "Delete ingredient", self.btn1Window)
        self.createbtn(self, "Add recipe", self.btn1Window)
        self.createbtn(self, "Edit recipe", self.btn1Window)
        self.createbtn(self, "Delete recipe", self.btn1Window)
        self.createbtn(self, "Add supplier", self.btn1Window)
        self.createbtn(self, "Edit supplier", self.btn1Window)
        self.createbtn(self, "Delete supplier", self.btn1Window)
        self.createbtn(self, "QUIT", self.master.destroy)

    def createbtn(self, master, text, command, *args):
        self.newButtn = tk.Button(master)
        self.newButtn["text"] = text
        self.newButtn["command"] = command
        if master != self:
            self.newButtn.grid(row=args[0], column=args[1], ipadx=10, ipady=6, padx=10, pady=10)
        else:
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
        self.btn1Window = tk.Toplevel(root)
        self.btn1Window.title("Add ingredient")
        self.ingr_group_id = tk.IntVar()
        self.calories = tk.StringVar()
        self.provider_id = tk.StringVar()
        self.ingredient_name = tk.StringVar()
        self.label1 = tk.Label(self.btn1Window, text="Ingredient group ID")
        self.label1.grid(row=0, column=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.label2 = tk.Label(self.btn1Window, text="Calories")
        self.label2.grid(row=0, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        self.label3 = tk.Label(self.btn1Window, text="Supplier ID")
        self.label3.grid(row=0, column=2, ipadx=10, ipady=6, padx=10, pady=10)
        self.label4 = tk.Label(self.btn1Window, text="Ingredient name")
        self.label4.grid(row=0, column=3, ipadx=10, ipady=6, padx=10, pady=10)
        self.group_entry = tk.Entry(master=self.btn1Window, textvariable=self.ingr_group_id)
        self.group_entry.grid(row=1, column=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.calories_entry = tk.Entry(master=self.btn1Window, textvariable=self.calories)
        self.calories_entry.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        self.provider_id_entry = tk.Entry(master=self.btn1Window, textvariable=self.provider_id)
        self.provider_id_entry.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)
        self.ingredient_name_entry = tk.Entry(master=self.btn1Window, textvariable=self.ingredient_name)
        self.ingredient_name_entry.grid(row=1, column=3, ipadx=10, ipady=6, padx=10, pady=10)
        self.createbtn(self.btn1Window, "Add", self.addtokb, 2, 1)
        self.createbtn(self.btn1Window, "QUIT", self.btn1Window.destroy, 2, 2)

    # def createEntery(self, master, textvariable):


    def addtokb(self):
        try:
            sql = """INSERT INTO ingredients(ingr_group_id, calories, provider_id, ingredient_name) 
            VALUES (%s, %s, %s, %s)""", (self.ingr_group_id, self.calories, self.provider_id, self.ingredient_name)
            # data = (self.ingr_group_id, self.calories, self.provider_id, self.ingredient_name)
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
        except Error as e:
            print(e)
        finally:
            conn.commit()
            cursor.close()
            self.disconnect(conn)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
