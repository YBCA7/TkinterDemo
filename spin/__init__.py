from tkinter import Toplevel
from spin._tk import SpinFrame
from spin._ttk import SpinTtkFrame


class SpinUI(Toplevel):
    def __init__(self, wm):
        super().__init__(wm)
        self.focus_set()
        self.title("Spinbox")
        SpinFrame(self).pack(padx=5, pady=5)
        SpinTtkFrame(self).pack(padx=5, pady=5)
