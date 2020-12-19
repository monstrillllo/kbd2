from tkinter import *


class NewListBox:
    def __init__(self, master, info):
        self.master = master
        self.info = info
        self.infstr = ""
        self.yscrollbar = Scrollbar(self.master)
        self.yscrollbar.pack(side=LEFT, fill=Y)
        self.NewListBox = Listbox(master=self.master, width=100, yscrollcommand=self.yscrollbar.set)

    def addInf(self):
        for inf in self.info:
            x = 0
            for i in inf:
                x += 1
                if x != len(inf):
                    self.infstr += str(i) + "--"
                else:
                    self.infstr += str(i)
            self.NewListBox.insert(END, self.infstr)
            self.infstr = ""
        return self.NewListBox
