from tkinter import Tk
from tkinter.ttk import Button
from basic import BasicUI
from spin import SpinUI
from listbox import ListboxUI
from common import setup


class App:
    def __init__(self, tk: Tk):
        self.root = tk
        self.root.title("All of Tkinter")
        self.areas = {
            "basic": Button(text="Basic Controls", width=40, command=lambda : BasicUI(self.root)),
            "spinbox": Button(text="Spinbox", width=40, command=lambda: SpinUI(self.root)),
            "listbox": Button(text="Listbox", width=40, command=lambda: ListboxUI(self.root))
        }
        setup(self.areas, 3)
