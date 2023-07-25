import tkinter as tk
from tkinter import ttk

# import sys
# import os.path

import sv_ttk


class App(ttk.Frame):
    def __init__(self, top=None):
        ttk.Frame.__init__(self)

        # top.geometry("584x710+639+65")  # 581x728+430+60
        top.geometry("500x500+400+100")  # 581x728+430+60
        top.minsize(120, 1)
        top.maxsize(1600, 880)
        top.resizable(0, 0)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for input widgets
        self.home = ttk.Frame(self, padding=(0, 0, 0, 10), borderwidth="2", width=450)
        self.home.place(relx=0.018, rely=0.022, relheight=0.944, relwidth=0.958)
        self.home.grid(row=0, column=0, padx=10, pady=(30, 10) , sticky="nsew", rowspan=3)

        # Create a Frame for the Checkbuttons
        self.homeFrame = ttk.LabelFrame(self.home, text="The Bank App", width=150, height=500)
        self.homeFrame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        # self.homeFrame = ttk.LabelFrame(self.home, text="The Bank App", padding=(20, 10), width=50, height=300)
        # self.homeFrame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        # Label
        self.sloganLabel = ttk.Label(self.homeFrame, text="Together we build a brighter future", justify="center")
        self.sloganLabel.grid(row=0, column=0, pady=10, columnspan=2)

        # Button
        self.button = ttk.Button(self.homeFrame, text="Button", width=50)
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Accentbutton
        self.accentbutton = ttk.Button(self.homeFrame, text="Accent button", style="Accent.TButton")
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

        # Togglebutton
        self.togglebutton = ttk.Checkbutton(self.homeFrame, text="Toggle button", style="Toggle.TButton")
        self.togglebutton.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")






if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bank App")

    # Simply set the theme # This is where the magic happens
    sv_ttk.set_theme("dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    # root.update()
    # root.minsize(root.winfo_width(), root.winfo_height())
    # x_coordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    # y_coordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    # root.geometry("+{}+{}".format(x_coordinate, y_coordinate-20))

    root.mainloop()
