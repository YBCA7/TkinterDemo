from tkinter import IntVar, BooleanVar
from tkinter.ttk import *
from tkinter.messagebox import *
from common import setup


class BasicTtkFrame(LabelFrame):
    def __init__(self, root):
        super().__init__(root)
        self.config(text="Ttk Basic Controls", borderwidth=5)
        self.vars = {
            "iv": IntVar(),
            "bv": BooleanVar()
        }
        self.widgets = {
            "label": Label(self, text="Label"),
            "button": Button(self, text="Button",
                command=self.button),

            "radio_0": Radiobutton(self, text="Radio 0", variable=self.vars["iv"], value=0, command=self.radio),
            "radio_1": Radiobutton(self, text="Radio 1", variable=self.vars["iv"], value=1, command=self.radio),
            "radio_2": Radiobutton(self, text="Radio 2", variable=self.vars["iv"], value=2, command=self.radio),
            "radio_3": Radiobutton(self, text="Radio 3", variable=self.vars["iv"], value=3, command=self.radio),
            "radio_4": Radiobutton(self, text="Radio 3", variable=self.vars["iv"], value=3, command=self.radio),

            "checkbutton": Checkbutton(self, text="Checkbutton", variable=self.vars["bv"]),
            "entry": Entry(self)
        }
        setup(self.widgets)

    def radio(self):
        showinfo("Information", f'You\'ve selected Radio {self.vars["iv"].get()}.')

    def button(self):
        showwarning("Warning", f"""Don't click that button again!
You've selected Radio {self.vars["iv"].get()} and the
Checkbutton is {"checked" if self.vars["bv"].get() else "unchecked"}.
You've entered "{self.widgets["entry"].get()}" in the entry.""")
