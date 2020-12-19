from tkinter import Button


class NewButtons:
    def __init__(self, master, text, command, row=None, column=None):
        self.master = master
        self.text = text
        self.command = command
        self.row = row
        self.column = column
        self.NewButtons = Button(master=self.master, text=self.text, command=command)
        self.NewButtons.grid(row=self.row, column=self.column, ipadx=10, ipady=6, padx=10, pady=10)
