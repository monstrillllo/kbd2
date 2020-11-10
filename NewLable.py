from tkinter import Label


class NewLable():
    def __init__(self, master, text, row, column):
        self.master = master
        self.text = text
        self.row = row
        self.column = column
        self.NewLable = Label(master=self.master, text=self.text)
        self.NewLable.grid(row=row, column=column, ipadx=10, ipady=6, padx=10, pady=10)
