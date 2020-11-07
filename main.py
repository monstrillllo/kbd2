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
        self.createbtn(self, "Edit ingredient", self.btn2Window)
        self.createbtn(self, "Delete ingredient", self.btn3Window)
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

    def btn1Window (self):
        self.btn1Window = tk.Toplevel(root)
        self.btn1Window.title("Add ingredient")

        self.ingr_group_id = tk.IntVar()
        self.calories = tk.StringVar()
        self.provider_id = tk.StringVar()
        self.ingredient_name = tk.StringVar()

        self.createLabel(self.btn1Window, "Ingredient group ID", 0, 0)
        self.createLabel(self.btn1Window, "Calories", 0, 1)
        self.createLabel(self.btn1Window, "Supplier ID", 0, 2)
        self.createLabel(self.btn1Window, "Ingredient name", 0, 3)

        self.createEntery(self.btn1Window, self.ingr_group_id, 1, 0)
        self.createEntery(self.btn1Window, self.calories, 1, 1)
        self.createEntery(self.btn1Window, self.provider_id, 1, 2)
        self.createEntery(self.btn1Window, self.ingredient_name, 1, 3)

        self.createbtn(self.btn1Window, "Add", self.addtokb, 2, 1)
        self.createbtn(self.btn1Window, "QUIT", self.btn1Window.destroy, 2, 2)

    def btn2Window(self):
        self.btn2Window = tk.Toplevel(root)
        self.btn2Window.title("Edit ingredient")

        self.igredient_edit = tk.StringVar
        self.new_ingr_group_id = tk.IntVar()
        self.new_calories = tk.StringVar()
        self.new_provider_id = tk.StringVar()
        self.new_ingredient_name = tk.StringVar()

        self.createLabel(self.btn2Window, "Ingredient to edit", 0, 0)
        self.createLabel(self.btn2Window, "New ingredient group ID", 0, 1)
        self.createLabel(self.btn2Window, "New calories", 0, 2)
        self.createLabel(self.btn2Window, "New supplier ID", 0, 3)
        self.createLabel(self.btn2Window, "New ingredient name", 0, 4)

        self.createEntery(self.btn2Window, self.igredient_edit, 1, 0)
        self.createEntery(self.btn2Window, self.new_ingr_group_id, 1, 1)
        self.createEntery(self.btn2Window, self.new_calories, 1, 2)
        self.createEntery(self.btn2Window, self.new_provider_id, 1, 3)
        self.createEntery(self.btn2Window, self.new_ingredient_name, 1, 4)

        self.createbtn(self.btn2Window, "Edit", self.addtokb, 2, 0)
        self.createbtn(self.btn2Window, "QUIT", self.btn2Window.destroy, 2, 4)

    def btn3Window(self):
        self.btn3Window = tk.Toplevel(root)
        self.btn3Window.title("Delete ingredient")

        self.igredient_delete = tk.StringVar

        self.createLabel(self.btn3Window, "Ingredient to delete", 0, 1)

        self.createEntery(self.btn3Window, self.igredient_delete, 1, 1)


        self.createbtn(self.btn3Window, "Delete", self.addtokb, 1, 0)
        self.createbtn(self.btn3Window, "QUIT", self.btn3Window.destroy, 1, 2)

    def createLabel(self, master, text, row, column):
        self.newLabel = tk.Label(master=master, text=text)
        self.newLabel.grid(row=row, column=column, ipadx=10, ipady=6, padx=10, pady=10)

    def createEntery(self, master, textvariable, row , column):
        self.new_entry = tk.Entry(master=master, textvariable=textvariable)
        self.new_entry.grid(row=row, column=column, ipadx=10, ipady=6, padx=10, pady=10)

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
root.title("Food")
app = Application(master=root)
app.mainloop()
