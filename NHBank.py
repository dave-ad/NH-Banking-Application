import tkinter as tk
from tkinter import ttk

# import sys
# import os.path

import sv_ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("")

    # Simply set the theme
    # This is where the magic happens
    sv_ttk.set_theme("dark")

    # app = App(root)
    # app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_coordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_coordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_coordinate, y_coordinate-20))

    root.mainloop()
