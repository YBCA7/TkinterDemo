from tkinter import Listbox, END
from tkinter.ttk import Frame, Label, Button, Entry
from tkinter.messagebox import showerror


class ListboxFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.widgets = {
            "listbox": Listbox(self, height=5),
            "l_item": Label(self, text="Item:"),
            "e_item": Entry(self),
            "b_add": Button(self, text="Add", command=self.add_item),
            "b_delete": Button(self, text="Delete", command=self.delete_item),
            "b_clear": Button(self, text="Clear", command=self.clear_items)
        }
        self.setup()

    def setup(self):
        self.widgets["listbox"].grid(row=0, columnspan=3, padx=5, pady=5, sticky="ew")
        self.widgets["l_item"].grid(row=1, column=0, padx=5, pady=5)
        self.widgets["e_item"].grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.widgets["b_add"].grid(row=1, column=2, padx=5, pady=5)
        self.widgets["b_delete"].grid(row=2, column=0, padx=5, pady=5)
        self.widgets["b_clear"].grid(row=2, column=1, padx=5, pady=5)

    def add_item(self):
        item = self.widgets["e_item"].get()
        if item:
            self.widgets["listbox"].insert(END, item)
            self.widgets["e_item"].delete(0, END)
        else:
            showerror("Error", "Please enter an item to add.")

    def delete_item(self):
        selection = self.widgets["listbox"].curselection()
        if selection:
            self.widgets["listbox"].delete(selection[0])

    def clear_items(self):
        self.widgets["listbox"].delete(0, END)
