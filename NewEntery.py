from tkinter import Entry


class NewEntery:
    def __init__(self, master, textvariable, row, column):
        self.textvariable = textvariable
        self.master = master
        self.row = row
        self.column = column
        self.newEntery = Entry(master=self.master, textvariable=self.textvariable)
        self.newEntery.grid(row=self.row, column=self.column, ipadx=10, ipady=6, padx=10, pady=10)
