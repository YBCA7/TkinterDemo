from tkinter import Toplevel
from listbox._tk import ListboxFrame


class ListboxUI(Toplevel):
    def __init__(self, wm):
        super().__init__(wm)
        self.focus_set()
        self.title("Listbox")
        ListboxFrame(self).pack(padx=5, pady=5, fill="x")
