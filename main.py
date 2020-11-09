import tkinter as tk
import connection
from querys import *


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

    def btn1Window(self):
        self.btn1Window = tk.Toplevel(root)
        self.btn1Window.title("Add ingredient")

        self.ingr_group_id = tk.IntVar()
        self.calories = tk.StringVar()
        self.provider_id = tk.IntVar()
        self.ingredient_name = tk.StringVar()

        self.createLabel(self.btn1Window, "Ingredient group ID", 0, 0)
        self.createLabel(self.btn1Window, "Calories", 0, 1)
        self.createLabel(self.btn1Window, "Supplier ID", 0, 2)
        self.createLabel(self.btn1Window, "Ingredient name", 0, 3)

        self.createEntery(self.btn1Window, self.ingr_group_id, 1, 0)
        self.createEntery(self.btn1Window, self.calories, 1, 1)
        self.createEntery(self.btn1Window, self.provider_id, 1, 2)
        self.createEntery(self.btn1Window, self.ingredient_name, 1, 3)

        self.createbtn(self.btn1Window, "Add", self.btn1Command, 2, 1)
        self.createbtn(self.btn1Window, "QUIT", self.btn1Window.destroy, 2, 2)

    def btn2Window(self):
        self.btn2Window = tk.Toplevel(root)
        self.btn2Window.title("Edit ingredient")

        self.igredient_to_edit = tk.StringVar()
        self.new_ingr_group_id = tk.IntVar()
        self.new_calories = tk.StringVar()
        self.new_provider_id = tk.IntVar()
        self.new_ingredient_name = tk.StringVar()

        self.createLabel(self.btn2Window, "Ingredient to edit", 0, 0)
        self.createLabel(self.btn2Window, "New ingredient group ID", 0, 1)
        self.createLabel(self.btn2Window, "New calories", 0, 2)
        self.createLabel(self.btn2Window, "New supplier ID", 0, 3)
        self.createLabel(self.btn2Window, "New ingredient name", 0, 4)

        self.createEntery(self.btn2Window, self.igredient_to_edit, 1, 0)
        self.createEntery(self.btn2Window, self.new_ingr_group_id, 1, 1)
        self.createEntery(self.btn2Window, self.new_calories, 1, 2)
        self.createEntery(self.btn2Window, self.new_provider_id, 1, 3)
        self.createEntery(self.btn2Window, self.new_ingredient_name, 1, 4)

        self.createbtn(self.btn2Window, "Edit", self.btn2Command, 2, 0)
        self.createbtn(self.btn2Window, "QUIT", self.btn2Window.destroy, 2, 4)

    def btn3Window(self):
        self.btn3Window = tk.Toplevel(root)
        self.btn3Window.title("Delete ingredient")

        self.igredient_delete = tk.StringVar()

        self.createLabel(self.btn3Window, "Ingredient to delete", 0, 1)

        self.createEntery(self.btn3Window, self.igredient_delete, 1, 1)

        self.createbtn(self.btn3Window, "Delete", self.btn3Command, 1, 0)
        self.createbtn(self.btn3Window, "QUIT", self.btn3Window.destroy, 1, 2)

    def createLabel(self, master, text, row, column):
        self.newLabel = tk.Label(master=master, text=text)
        self.newLabel.grid(row=row, column=column, ipadx=10, ipady=6, padx=10, pady=10)

    def createEntery(self, master, textvariable, row, column):
        self.new_entry = tk.Entry(master=master, textvariable=textvariable)
        self.new_entry.grid(row=row, column=column, ipadx=10, ipady=6, padx=10, pady=10)

    def btn1Command(self):
        val = (self.ingr_group_id.get(), self.calories.get(), self.provider_id.get(), self.ingredient_name.get())
        connection.addtokb(AddIngr, val)
        self.btn1Window.destroy()

    def btn2Command(self):
        val = (self.new_ingr_group_id.get(), self.new_calories.get(), self.new_provider_id.get(),
               self.new_ingredient_name.get(), self.igredient_to_edit.get())
        connection.addtokb(EditIngr, val)
        self.btn2Window.destroy()

    def btn3Command(self):
        val = (self.igredient_delete.get())
        connection.addtokb(DeleteIngr, val)
        self.btn3Window.destroy()


root = tk.Tk()
root.title("Food")
app = Application(master=root)
app.mainloop()
