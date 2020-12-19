from tkinter import StringVar
from tkinter import Toplevel
from tkinter import Listbox

from NewButtons import *
from NewLable import *
from NewEntery import *
from connection import *
from querys import *
from NewListBox import *


class TopLevelWindow():
    def __init__(self, master, title, *args):
        self.master = master
        self.title = title
        self.lables = args
        self.newVariable = None
        self.variables = []
        self.info = None
        self.row = 0
        self.column = 0
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("%s" % self.title)
        if (self.title != "Food-Recipe list") and (self.title != "Low-calorie dish"):
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

    def ToTable(self, query):
        c1 = connection(query)
        self.info = c1.selectWithoutParams()
        lb1 = NewListBox(self.newWindow, self.info)
        lb2 = lb1.addInf()
        lb2.pack()

    def tokb(self):
        val = []
        for vari in self.variables:
            val.append(vari.get())
        if self.title == "Add ingredient":
            c1 = connection(AddIngr, val)
            c1.addtokb()
            self.newWindow.destroy()
        elif self.title == "Edit ingredient":
            c2 = connection(EditIngr, val)
            c2.addtokb()
            self.newWindow.destroy()
        elif self.title == "Delete ingredient":
            c3 = connection(DeleteIngr, val)
            c3.addtokb()
            self.newWindow.destroy()

        elif self.title == "Add recipe":
            c4 = connection(AddRecipe, val)
            c4.addtokb()
            self.newWindow.destroy()
        elif self.title == "Edit recipe":
            c5 = connection(EditRecipe, val)
            c5.addtokb()
            self.newWindow.destroy()
        elif self.title == "Delete recipe":
            c6 = connection(DeleteRecipe, val)
            c6.addtokb()
            self.newWindow.destroy()

        elif self.title == "Add supplier":
            c7 = connection(AddSupplier, val)
            c7.addtokb()
            self.newWindow.destroy()
        elif self.title == "Edit supplier":
            c8 = connection(EditSupplier, val)
            c8.addtokb()
            self.newWindow.destroy()
        elif self.title == "Delete supplier":
            c9 = connection(DeleteSupplier, val)
            c9.addtokb()
            self.newWindow.destroy()

        elif self.title == "Price list":
            c10 = connection(PriceList, val)
            self.info = c10.selectfromkb()
            ListWindow = Toplevel(self.master)
            lb1 = NewListBox(ListWindow, self.info)
            lb2 = lb1.addInf()
            lb2.pack()
            self.newWindow.destroy()

        elif self.title == "Low-calorie dish":
            c11 = connection(Low_calorie_dish, val)
            self.info = c11.selectfromkb()
            ListWindow = Toplevel(self.master)
            lb1 = NewListBox(ListWindow, self.info)
            lb2 = lb1.addInf()
            lb2.pack()
            self.newWindow.destroy()
