from tkinter.ttk import *
from tkinter.messagebox import showerror


class SpinTtkFrame(LabelFrame):
    def __init__(self, root):
        super().__init__(root)
        self.config(text="Ttk Spinbox", borderwidth=5)
        self.widgets = {
            "spinbox": Spinbox(self),
            "lf": Label(self, text="From:"),
            "ef": Entry(self),
            "lt": Label(self, text="To:"),
            "et": Entry(self),
            "li": Label(self, text="increment:"),
            "ei": Entry(self),
            "b": Button(self, text="Set", command=self.set, width=50)
        }
        self.setup()

    def setup(self):
        self.widgets["spinbox"].grid(row=0, columnspan=3, padx=5, pady=5)
        self.widgets["lf"].grid(row=1, column=0, padx=5, pady=5)
        self.widgets["ef"].grid(row=2, column=0, padx=5, pady=5)
        self.widgets["lt"].grid(row=1, column=1, padx=5, pady=5)
        self.widgets["et"].grid(row=2, column=1, padx=5, pady=5)
        self.widgets["li"].grid(row=1, column=2, padx=5, pady=5)
        self.widgets["ei"].grid(row=2, column=2, padx=5, pady=5)
        self.widgets["b"].grid(row=3, columnspan=3, padx=5, pady=5)

    def set(self):
        try:
            self.widgets["spinbox"].config(
                from_=float(self.widgets["ef"].get()),
                to=float(self.widgets["et"].get()),
                increment=float(self.widgets["ei"].get()),
            )
        except ValueError:
            showerror("Error", "The value can't be set into the Spinbox.")
