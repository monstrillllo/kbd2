import tkinter as tk

from TopLevelWindow import *
from querys import *


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

        NewButtons(self, "Price list", self.btn10Window, 3, 0)
        NewButtons(self, "Food-Recipe list", self.btn11Window, 3, 1)
        NewButtons(self, "Low-calorie dish", self.btn12Window, 3, 2)

        NewButtons(self, "QUIT", self.master.destroy, 4, 2)

    def btn1Window(self):
        TopLevelWindow(self.master, "Add ingredient", "Ingredient group ID",
                       "Calories", "Supplier ID", "Ingredient name")

    def btn2Window(self):
        TopLevelWindow(self.master, "Edit ingredient", "New ingredient group ID",
                       "New calories", "New supplier ID", "New ingredient name", "Ingredient to edit")

    def btn3Window(self):
        TopLevelWindow(self.master, "Delete ingredient", "Ingredient name")

    def btn4Window(self):
        TopLevelWindow(self.master, "Add recipe", "Recipe ID",
                       "Recipe name", "Description", "Author ID")

    def btn5Window(self):
        TopLevelWindow(self.master, "Edit recipe", "New recipe ID", "New recipe name", "New description",
                       "New author ID", "Recipe to edit")

    def btn6Window(self):
        TopLevelWindow(self.master, "Delete recipe", "Recipe name")

    def btn7Window(self):
        TopLevelWindow(self.master, "Add supplier", "Supplier ID",
                       "Supplier name", "Address", "Phone")

    def btn8Window(self):
        TopLevelWindow(self.master, "Edit supplier", "New supplier ID", "New supplier name",
                       "New address", "New phone", "Supplier to edit")

    def btn9Window(self):
        TopLevelWindow(self.master, "Delete supplier", "Supplier name")

    def btn10Window(self):
        TopLevelWindow(self.master, "Price list", "Supplier id", "Date")

    def btn11Window(self):
        w1 = TopLevelWindow(self.master, "Food-Recipe list")
        w1.ToTable(Food_RecipeList)

    def btn12Window(self):
        w2 = TopLevelWindow(self.master, "Low-calorie dish")
        w2.ToTable(Low_calorie_dish)
