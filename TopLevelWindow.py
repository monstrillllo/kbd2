from tkinter import StringVar
from tkinter import Toplevel

from NewButtons import *
from NewLable import *
from NewEntery import *
from connection import *
from querys import *


class TopLevelWindow():
    def __init__(self, master, title, *args):
        self.master = master
        self.title = title
        self.lables = args
        self.newVariable = None
        self.variables = []
        self.row = 0
        self.column = 0
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("%s" % self.title)
        self.addLables()
        self.addEntery()
        self.addButtons()

    def addLables(self):
        for lab in self.lables:
            NewLable(self.newWindow, lab, self.row, self.column)
            self.column += 1
        self.column = 0
        self.row += 1

    def addButtons(self):
        NewButtons(self.newWindow, self.title, self.tokb, self.row, 0)
        NewButtons(self.newWindow, "QUIT", self.newWindow.destroy, self.row, 1)
        self.row += 1

    def addEntery(self):
        for lab in self.lables:
            self.newVariable = StringVar()
            self.variables.append(self.newVariable)
            NewEntery(self.newWindow, self.newVariable, self.row, self.column)
            self.column += 1
        self.column = 0
        self.row += 1

    def tokb(self):
        val = []
        for vari in self.variables:
            val.append(vari.get())
        if self.title == "Add ingredient":
            connection(AddIngr, val)
        if self.title == "Edit ingredient":
            connection(EditIngr, val)
        if self.title == "Delete ingredient":
            connection(DeleteIngr, val)

        if self.title == "Add recipe":
            connection(AddRecipe, val)
        if self.title == "Edit recipe":
            connection(EditRecipe, val)
        if self.title == "Delete recipe":
            connection(DeleteRecipe, val)

        if self.title == "Add Supplier":
            connection(AddSupplier, val)
        if self.title == "Edit Supplier":
            connection(EditSupplier, val)
        if self.title == "Delete Supplier":
            connection(DeleteSupplier, val)
        self.newWindow.destroy()
