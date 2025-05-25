def setup(widgets: dict, max_width: int = 7):
    r, c = 0, 0
    for control in widgets.values():
        if c < max_width:
            control.grid(row=r, column=c, padx=5, pady=5)
            c += 1
        else:
            r += 1
            c = 0
            control.grid(row=r, column=c, padx=5, pady=5)
            c += 1
