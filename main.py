import tkinter as tk
from connection import *
from querys import *
from TopLevelWindow import *
from NewLable import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        NewButtons(self, "Add ingredient", self.btn1Window, 0, 0)
        NewButtons(self, "Edit ingredient", self.btn2Window, 0, 1)
        NewButtons(self, "Delete ingredient", self.btn3Window, 0, 2)

        NewButtons(self, "Add recipe", self.btn4Window, 1, 0)
        NewButtons(self, "Edit recipe", self.btn5Window, 1, 1)
        NewButtons(self, "Delete recipe", self.btn6Window, 1, 2)

        NewButtons(self, "Add Supplier", self.btn7Window, 2, 0)
        NewButtons(self, "Edit Supplier", self.btn8Window, 2, 1)
        NewButtons(self, "Delete Supplier", self.btn9Window, 2, 2)

        NewButtons(self, "QUIT", self.master.destroy, 3, 2)

    def btn1Window(self):
        TopLevelWindow(root, "Add ingredient", "Ingredient group ID",
                       "Calories", "Supplier ID", "Ingredient name")

    def btn2Window(self):
        TopLevelWindow(root, "Edit ingredient", "Ingredient to edit", "New ingredient group ID",
                       "New calories", "New supplier ID", "New ingredient name")

    def btn3Window(self):
        TopLevelWindow(root, "Delete ingredient", "Ingredient name")

    def btn4Window(self):
        TopLevelWindow(root, "Add recipe", "Recipe ID",
                       "Recipe name", "Description", "Author ID")

    def btn5Window(self):
        TopLevelWindow(root, "Edit recipe", "Recipe to edit",
                       "New recipe ID", "New recipe name", "New description", "New author ID")

    def btn6Window(self):
        TopLevelWindow(root, "Delete recipe", "Recipe name")

    def btn7Window(self):
        TopLevelWindow(root, "Add supplier", "Supplier ID",
                       "Supplier name", "Address", "Phone")

    def btn8Window(self):
        TopLevelWindow(root, "Edit supplier", "Supplier to edit",
                       "New supplier ID", "New supplier name", "New address", "New phone")

    def btn9Window(self):
        TopLevelWindow(root, "Delete supplier", "Supplier name")


root = tk.Tk()
root.title("Food")
app = Application(master=root)
app.mainloop()
