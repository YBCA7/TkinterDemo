from tkinter import Toplevel
from basic._tk import BasicFrame
from basic._ttk import BasicTtkFrame


class BasicUI(Toplevel):
    def __init__(self, wm):
        super().__init__(wm)
        self.focus_set()
        self.title("Basic Controls")
        BasicFrame(self).pack(padx=5, pady=5)
        BasicTtkFrame(self).pack(padx=5, pady=5)
