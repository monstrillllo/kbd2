from tkinter import *


class NewListBox:
    def __init__(self, master, info):
        self.master = master
        self.info = info
        #self.xscrollbar = Scrollbar(self.master, orient=HORIZONTAL)
        #self.xscrollbar.pack(side=BOTTOM, fill=X)
        self.yscrollbar = Scrollbar(self.master)
        self.yscrollbar.pack(side=LEFT, fill=Y)
        self.NewListBox = Listbox(master=self.master, width=100, yscrollcommand=self.yscrollbar.set)

    def addInf(self):
        for inf in self.info:
            self.NewListBox.insert(END, inf)
        return self.NewListBox
