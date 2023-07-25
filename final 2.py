__author__ = "AD"
"""
Refactored on Tue Jul 24 10:07:27 2021

@author: AD
Refactoring EDHAC banking software to create a more mordern UI and backend
"""

import sys
# from PIL import Image, ImageTk

# import ecommerce_support
import os.path

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

# import final_support

import os.path

import mysql.connector

import re

from tkinter import messagebox

import random

import socket
import shelve

import json

import threading
import time


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    # final_support.set_Tk_po0-
    top = Toplevel1(root)
    # final_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    # final_support.set_Tk_var()
    top = Toplevel1(w)
    # final_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("584x710+639+65")  # 581x728+430+60
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("EDHAC BANK")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        # ----------CREATE MYSQL CONNECTION---------------------------------
        self.conn = mysql.connector.connect(host="localhost", database="", user="root", password="")
        self.cursor = self.conn.cursor()

        # -----------------------CREATE TCP/IP SERVER CONNECTION----------------
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 8000
        self.s.connect((host, port))

        # ----------------------------LANDING PAGE (HOME PAGE)-----------------------------------
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#000000")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.042, rely=0.015, height=121, width=144)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img5
        # _img5 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img5)
        self.Label1.configure(text='''Label''')

        # HEADER
        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.26, rely=0.244, relheight=0.096, relwidth=0.461)
        self.Message1.configure(background="#e8e800")
        self.Message1.configure(font="-family {Verdana} -size 16 -weight bold -slant italic")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''EDHAC BANK''')
        self.Message1.configure(width=230)

        # BANK SLOGAN
        self.Message2 = tk.Message(self.Frame1)
        self.Message2.place(relx=0.148, rely=0.336, relheight=0.067, relwidth=0.681)
        self.Message2.configure(background="#000000")
        self.Message2.configure(font="-family {Lucida Calligraphy} -size 11")
        self.Message2.configure(foreground="#ffffff")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''Together we can build a brighter future''')
        self.Message2.configure(width=340)

        # OPEN ACCOUNT BUTTON
        self.accButton1 = tk.Button(self.Frame1, command=lambda: self.show_frame(self.Create))
        self.accButton1.place(relx=0.201, rely=0.458, height=40, width=340)
        self.accButton1.configure(activebackground="#f9f9f9")
        self.accButton1.configure(activeforeground="black")
        self.accButton1.configure(background="#ffffff")
        self.accButton1.configure(borderwidth="0")
        self.accButton1.configure(disabledforeground="#a3a3a3")
        self.accButton1.configure(font="-family {Times New Roman} -size 9")
        self.accButton1.configure(foreground="#000000")
        self.accButton1.configure(highlightbackground="#d9d9d9")
        self.accButton1.configure(highlightcolor="black")
        self.accButton1.configure(pady="0")
        self.accButton1.configure(relief="groove")
        self.accButton1.configure(text='''OPEN AN ACCOUNT''')

        # REGISTER BUTTON
        self.Button1_1 = tk.Button(self.Frame1, command=lambda: self.show_frame(self.Registration))
        self.Button1_1.place(relx=0.201, rely=0.595, height=40, width=340)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#ffffff")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Times New Roman} -size 9")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''REGISTER''')

        # LOGIN BUTTON
        self.Button1_2 = tk.Button(self.Frame1, command=lambda: self.show_frame(self.login))
        self.Button1_2.place(relx=0.201, rely=0.733, height=40, width=340)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#ffffff")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(font="-family {Times New Roman} -size 9")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''LOGIN''')

        # -----------------------CREATE ACCOUNT----------------
        self.Create = tk.Frame(top)
        self.Create.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.Create.configure(relief='groove')
        self.Create.configure(borderwidth="2")
        self.Create.configure(relief="groove")
        self.Create.configure(background="#ffffff")
        self.Create.configure(highlightbackground="#d9d9d9")
        self.Create.configure(highlightcolor="white")

        # LOGO
        self.Label21 = tk.Label(self.Create)
        self.Label21.place(x=20, y=10, height=98, width=138)
        self.Label21.configure(background="#ffffff")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img1
        # _img1 = ImageTk.PhotoImage(file=photo_location)
        # self.Label21.configure(image=_img1)
        self.Label21.configure(text='''Label''')

        # HOME BUTTON
        self.Button2 = tk.Button(self.Create, command=lambda: self.show_frame(self.Frame1))
        self.Button2.place(x=400, y=34, height=34, width=77)
        self.Button2.configure(activebackground="#e8e800")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#000000")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Button2.configure(foreground="#e8e800")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Home''')

        # LOGIN BUTTON
        self.Button3 = tk.Button(self.Create, command=lambda: self.show_frame(self.login))
        self.Button3.place(x=493, y=34, height=34, width=77)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#000000")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Button3.configure(foreground="#e8e800")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Login''')

        # LABEL FRAME
        self.Labelframe3 = tk.LabelFrame(self.Create)
        self.Labelframe3.place(x=19, y=116, height=602, width=554)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(font="-family {Arial} -size 11 -slant italic")
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Creating account''')
        self.Labelframe3.configure(background="#ffffff")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="white")

        # FULLNAME LABEL
        self.Label4 = tk.Label(self.Labelframe3)
        self.Label4.place(x=11, y=50, height=35, width=66, bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#000000")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Verdana} -size 10 -weight bold")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Fullname''')

        # FULLNAME ENTRY
        self.Entry3 = tk.Entry(self.Labelframe3)
        self.Entry3.place(x=41, y=99, height=20, width=204, bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="blue")
        self.Entry3.configure(selectforeground="white")

        # EMAIL LABEL
        self.Label5 = tk.Label(self.Labelframe3)
        self.Label5.place(x=11, y=146, height=36, width=86, bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#000000")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Label5.configure(foreground="#ffffff")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''E-mail''')

        # EMAIL ENTRY
        self.Entry4 = tk.Entry(self.Labelframe3)
        self.Entry4.place(x=41, y=204, height=20, width=204, bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="blue")
        self.Entry4.configure(selectforeground="white")

        # D.O.B LABEL
        self.Label6 = tk.Label(self.Labelframe3)
        self.Label6.place(x=11, y=249, height=36, width=68, bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#000000")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Label6.configure(foreground="#ffffff")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''D.O.B''')

        # D.O.B ENTRY
        self.Entry5 = tk.Entry(self.Labelframe3)
        self.Entry5.place(x=41, y=299, height=20, width=204, bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="blue")
        self.Entry5.configure(selectforeground="white")

        # PHONE NUMBER LABEL
        self.Label7 = tk.Label(self.Labelframe3)
        self.Label7.place(x=11, y=349, height=36, width=68, bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#000000")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Label7.configure(foreground="#ffffff")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Phone''')

        # PHONE NUMBER ENTRY
        self.Entry6 = tk.Entry(self.Labelframe3)
        self.Entry6.place(x=41, y=406, height=20, width=204, bordermode='ignore')
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="blue")
        self.Entry6.configure(selectforeground="white")

        # ADDRESS LABEL
        self.Label8 = tk.Label(self.Labelframe3)
        self.Label8.place(x=11, y=465, height=36, width=90, bordermode='ignore')
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#000000")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Label8.configure(foreground="#ffffff")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Address''')

        # ADDRESS ENTRY
        self.Entry7 = tk.Entry(self.Labelframe3)
        self.Entry7.place(x=41, y=514, height=20, width=204, bordermode='ignore')
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="blue")
        self.Entry7.configure(selectforeground="white")

        # SPERATOR LINE
        self.TSeparator1 = ttk.Separator(self.Labelframe3)
        self.TSeparator1.place(x=266, y=23, height=0, bordermode='ignore')
        self.TSeparator1.configure(orient="vertical")

        # GENDER LABEL
        self.Label9_1 = tk.Label(self.Labelframe3)
        self.Label9_1.place(x=277, y=20, height=52, width=89, bordermode='ignore')
        self.Label9_1.configure(activebackground="#f9f9f9")
        self.Label9_1.configure(activeforeground="black")
        self.Label9_1.configure(background="#ffffff")
        self.Label9_1.configure(disabledforeground="#a3a3a3")
        self.Label9_1.configure(font="-family {Verdana} -size 12 -weight bold")
        self.Label9_1.configure(foreground="#000000")
        self.Label9_1.configure(highlightbackground="#d9d9d9")
        self.Label9_1.configure(highlightcolor="black")
        self.Label9_1.configure(text='''Gender:''')

        # MALE LABEL
        self.Label13 = tk.Label(self.Labelframe3)
        self.Label13.place(x=288, y=72, height=35, width=51, bordermode='ignore')
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(background="#ffffff")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font="-family {Verdana} -size 11")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''Male''')

        # MALE RADIOBUTTON
        self.rad1 = tk.IntVar()
        self.Radiobutton1 = tk.Radiobutton(self.Labelframe3)
        self.Radiobutton1.place(x=338, y=72, height=42, width=39, bordermode='ignore')
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(variable=self.rad1)

        # FEMALE LABEL
        self.Label14 = tk.Label(self.Labelframe3)
        self.Label14.place(x=370, y=72, height=35, width=73, bordermode='ignore')
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(background="#ffffff")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font="-family {Verdana} -size 11")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''Female''')

        # FEMALE RADIOBUTTON
        self.rad2 = tk.IntVar()
        self.Radiobutton2 = tk.Radiobutton(self.Labelframe3)
        self.Radiobutton2.place(x=452, y=72, height=42, width=59, bordermode='ignore')
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(variable=self.rad2)
        
        # MARITAL STATUS LABEL
        self.Label9 = tk.Label(self.Labelframe3)
        self.Label9.place(x=277, y=133, height=51, width=145, bordermode='ignore')
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Verdana} -size 12 -weight bold")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Marital Status :''')

        # MARRIED LABEL
        self.Label10 = tk.Label(self.Labelframe3)
        self.Label10.place(x=400, y=210, height=37, width=83, bordermode='ignore')
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#ffffff")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Verdana} -size 11")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Married''')

        # MARRIED LABEL BUTTON
        self.rad4 = tk.IntVar()
        self.Radiobutton4 = tk.Radiobutton(self.Labelframe3)
        self.Radiobutton4.place(x=493, y=210, height=42, width=28, bordermode='ignore')
        self.Radiobutton4.configure(activebackground="#ececec")
        self.Radiobutton4.configure(activeforeground="#000000")
        self.Radiobutton4.configure(background="#ffffff")
        self.Radiobutton4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton4.configure(foreground="#000000")
        self.Radiobutton4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton4.configure(highlightcolor="black")
        self.Radiobutton4.configure(justify='left')
        self.Radiobutton4.configure(variable=self.rad4)

        # SINGLE LABEL
        self.Label11 = tk.Label(self.Labelframe3)
        self.Label11.place(x=288, y=195, height=70, width=66, bordermode='ignore')
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#ffffff")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Verdana} -size 11")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Single''')

        # SINGLE RADIO BUTTON
        self.rad3 = tk.IntVar()
        self.Radiobutton3 = tk.Radiobutton(self.Labelframe3)
        self.Radiobutton3.place(x=359, y=210, height=42, width=29, bordermode='ignore')
        self.Radiobutton3.configure(activebackground="#ececec")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#ffffff")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify='left')
        self.Radiobutton3.configure(variable=self.rad3)

        # TYPE OF ACCOUNT LABEL
        self.Label12 = tk.Label(self.Labelframe3)
        self.Label12.place(x=277, y=287, height=35, width=168, bordermode='ignore')
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#ffffff")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font="-family {Verdana} -size 12 -weight bold")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''Type of Account :''')

        # SAVINGS LABEL
        self.Label15 = tk.Label(self.Labelframe3)
        self.Label15.place(x=297, y=338, height=35, width=89, bordermode='ignore')
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(activeforeground="black")
        self.Label15.configure(background="#ffffff")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(font="-family {Verdana} -size 11")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(highlightbackground="#d9d9d9")
        self.Label15.configure(highlightcolor="black")
        self.Label15.configure(text='''Savings :''')

        # SAVINGS RADIOBUTTON
        self.rad5 = tk.IntVar()
        self.Radiobutton5 = tk.Radiobutton(self.Labelframe3)
        self.Radiobutton5.place(x=400, y=338, height=42, width=59, bordermode='ignore')
        self.Radiobutton5.configure(activebackground="#ececec")
        self.Radiobutton5.configure(activeforeground="#000000")
        self.Radiobutton5.configure(background="#ffffff")
        self.Radiobutton5.configure(disabledforeground="#a3a3a3")
        self.Radiobutton5.configure(foreground="#000000")
        self.Radiobutton5.configure(highlightbackground="#d9d9d9")
        self.Radiobutton5.configure(highlightcolor="black")
        self.Radiobutton5.configure(justify='left')
        self.Radiobutton5.configure(variable=self.rad5)

        # CURRENT LABEL
        self.Label16 = tk.Label(self.Labelframe3)
        self.Label16.place(x=297, y=400, height=35, width=97, bordermode='ignore')
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(font="-family {Verdana} -size 11")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(text='''Current :''')

        # CURRENT LABELBUTTON
        self.rad6 = tk.IntVar()
        self.Radiobutton6 = tk.Radiobutton(self.Labelframe3)
        self.Radiobutton6.place(x=400, y=400, height=42, width=59, bordermode='ignore')
        self.Radiobutton6.configure(activebackground="#ececec")
        self.Radiobutton6.configure(activeforeground="#000000")
        self.Radiobutton6.configure(background="#ffffff")
        self.Radiobutton6.configure(disabledforeground="#a3a3a3")
        self.Radiobutton6.configure(foreground="#000000")
        self.Radiobutton6.configure(highlightbackground="#d9d9d9")
        self.Radiobutton6.configure(highlightcolor="black")
        self.Radiobutton6.configure(justify='left')
        self.Radiobutton6.configure(variable=self.rad6)

        # CREATE ACCOUNT BUTTON
        self.Button6 = tk.Button(self.Labelframe3, command=lambda: self.show_frame(self.T_and_C))
        self.Button6.place(x=329, y=482, height=34, width=157, bordermode='ignore')
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#000000")
        self.Button6.configure(borderwidth="1")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font="-family {Verdana} -size 11 -weight bold")
        self.Button6.configure(foreground="#e8e800")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Create Account''')

        # -----------------------TERMS AND CONDITION----------------
        self.T_and_C = tk.Frame(top)
        self.T_and_C.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.T_and_C.configure(relief='groove')
        self.T_and_C.configure(borderwidth="2")
        self.T_and_C.configure(relief="groove")
        self.T_and_C.configure(background="#ffffff")
        self.T_and_C.configure(cursor="fleur")
        self.T_and_C.configure(highlightbackground="#d9d9d9")
        self.T_and_C.configure(highlightcolor="black")

        # LABELFRAME
        self.Labelframe1 = tk.LabelFrame(self.T_and_C)
        self.Labelframe1.place(x=11, y=40, height=680, width=553)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {Verdana} -size 10 -weight bold -slant italic")
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''TERMS AND CONDITIONS''')
        self.Labelframe1.configure(background="#ffffff")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        # T & C MESSAGE
        self.Message1 = tk.Message(self.Labelframe1)
        self.Message1.place(x=10, y=56, height=409, width=510, bordermode='ignore')
        self.Message1.configure(background="#ff0000")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#ffffff")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''loremm''')
        self.Message1.configure(width=531)

        # T & C CHECKBOX
        self.che48 = tk.StringVar()
        self.Checkbutton1 = tk.Checkbutton(self.Labelframe1)
        self.Checkbutton1.place(x=97, y=494, height=61, width=350, bordermode='ignore')
        self.Checkbutton1.configure(activebackground="#ffffff")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#ffffff")
        self.Checkbutton1.configure(cursor="fleur")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#ffffff")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(offrelief="flat")
        self.Checkbutton1.configure(text='''I agree to the terms and conditions''')
        self.Checkbutton1.configure(relief="groove")
        self.Checkbutton1.configure(variable=self.che48)

        # AGREE BUTTON
        self.Button4 = tk.Button(self.Labelframe1, command=lambda: self.validation_acc_thread(None))
        self.Button4.place(x=78, y=585, height=34, width=129, bordermode='ignore')
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#000000")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Verdana} -size 10 -weight bold")
        self.Button4.configure(foreground="#e8e800")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Agree''')

        # DISMISS BUTTON
        self.Button5 = tk.Button(self.Labelframe1, command=lambda: self.show_frame(self.Frame1))
        self.Button5.place(x=301, y=585, height=34, width=129, bordermode='ignore')
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#000000")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Verdana} -size 10 -weight bold")
        self.Button5.configure(foreground="#e8e800")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Dismiss''')
        
        # -----------------------lOGIN----------------
        # CREATING LOGIN FRAME
        self.login = tk.Frame(top)
        self.login.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.login.configure(relief='groove')
        self.login.configure(borderwidth="2")
        self.login.configure(relief="groove")
        self.login.configure(background="#ffffff")
        self.login.configure(highlightbackground="#d9d9d9")
        self.login.configure(highlightcolor="black")

        # LOGO
        self.Label23 = tk.Label(self.login)
        self.Label23.place(x=19, y=10, height=103, width=151)
        self.Label23.configure(background="#d9d9d9")
        self.Label23.configure(disabledforeground="#a3a3a3")
        self.Label23.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img0
        # _img0 = ImageTk.PhotoImage(file=photo_location)
        # self.Label23.configure(image=_img0)
        self.Label23.configure(text='''Label''')

        # HOME BUTTON
        self.Button10 = tk.Button(self.login, command=lambda: self.show_frame(self.Frame1))
        self.Button10.place(x=381, y=29, height=34, width=77)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#000000")
        self.Button10.configure(borderwidth="1")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Button10.configure(foreground="#e8e800")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''Home''')

        # REGISTER BUTTON
        self.Button11 = tk.Button(self.login, command=lambda: self.show_frame(self.Registration))
        self.Button11.place(x=487, y=29, height=34, width=77)
        self.Button11.configure(activebackground="#ececec")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#000000")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Button11.configure(foreground="#e8e800")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''Register''')

        # LABEL FRAME
        self.Labelframe2 = tk.LabelFrame(self.login)
        self.Labelframe2.place(x=39, y=145, height=453, width=522)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''LOGIN''')
        self.Labelframe2.configure(background="#ffffff")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        # USERNAME
        self.Label2 = tk.Label(self.Labelframe2)
        self.Label2.place(x=29, y=86, height=33, width=108, bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Verdana} -size 12 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Username :''')

        # USER-PIN
        self.Label3 = tk.Label(self.Labelframe2)
        self.Label3.place(x=19, y=148, height=40, width=116, bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Verdana} -size 11 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Pin :''')

        # USERNAME ENTRY
        self.Entry1 = tk.Entry(self.Labelframe2)
        self.Entry1.place(x=166, y=90, height=27, width=204, bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        # USER-PIN ENTRY
        self.Entry2 = tk.Entry(self.Labelframe2)
        self.Entry2.place(x=166, y=159, height=27, width=204, bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        # LOGIN BUTTON
        self.Button1 = tk.Button(self.Labelframe2,command=lambda: self.authentication_thread(None))
        self.Button1.place(x=156, y=240, height=34, width=150, bordermode='ignore')
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#000000")
        self.Button1.configure(cursor="arrow")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Verdana} -size 10 -weight bold")
        self.Button1.configure(foreground="#e8e800")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')

        # ------------------REGISTRATION PAGE---------------------------
        self.Registration = tk.Frame(top)
        self.Registration.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.Registration.configure(relief='groove')
        self.Registration.configure(borderwidth="2")
        self.Registration.configure(relief="groove")
        self.Registration.configure(background="#ffffff")
        self.Registration.configure(highlightbackground="#ffffff")
        self.Registration.configure(highlightcolor="black")

        # LOGO
        self.Label17 = tk.Label(self.Registration)
        self.Label17.place(x=11, y=10, height=102, width=192)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(background="#ffffff")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img2
        # _img2 = ImageTk.PhotoImage(file=photo_location)
        # self.Label17.configure(image=_img2)
        self.Label17.configure(text='''Label''')

        # HOME BUTTON
        self.Button8 = tk.Button(self.Registration, command=lambda: self.show_frame(self.Frame1))
        self.Button8.place(x=345, y=30, height=34, width=77)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#000000")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Button8.configure(foreground="#e8e800")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Home''')

        # CREATE ACCOUNT BUTTON
        self.Button9 = tk.Button(self.Registration, command=lambda: self.show_frame(self.Create))
        self.Button9.place(x=444, y=30, height=34, width=115)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#000000")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Button9.configure(foreground="#e8e800")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Create account''')

        # REGISTRATION LABEL
        self.Label18 = tk.Label(self.Registration)
        self.Label18.place(x=167, y=178, height=54, width=171)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(activeforeground="black")
        self.Label18.configure(background="#ffffff")
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(font="-family {Times New Roman} -size 20 -weight bold -slant italic")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(highlightbackground="#d9d9d9")
        self.Label18.configure(highlightcolor="black")
        self.Label18.configure(text='''Registration''')

        # ACCOUNT NUMBER LABEL
        self.Label19 = tk.Label(self.Registration)
        self.Label19.place(x=21, y=267, height=39, width=167)
        self.Label19.configure(activebackground="#f9f9f9")
        self.Label19.configure(activeforeground="black")
        self.Label19.configure(background="#ffffff")
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(font="-family {Verdana} -size 11 -weight bold")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(highlightbackground="#d9d9d9")
        self.Label19.configure(highlightcolor="black")
        self.Label19.configure(text='''Account number :''')

        # ACCOUNT NUMBER ENTRY
        self.Entry8 = tk.Entry(self.Registration)
        self.Entry8.place(x=209, y=273, height=27, width=200)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(highlightbackground="#d9d9d9")
        self.Entry8.configure(highlightcolor="black")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(selectbackground="blue")
        self.Entry8.configure(selectforeground="white")

        # USERNAME LABEL
        self.Label20 = tk.Label(self.Registration)
        self.Label20.place(x=42, y=337, height=38, width=119)
        self.Label20.configure(activebackground="#f9f9f9")
        self.Label20.configure(activeforeground="black")
        self.Label20.configure(background="#ffffff")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(font="-family {Verdana} -size 11 -weight bold")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(highlightbackground="#d9d9d9")
        self.Label20.configure(highlightcolor="black")
        self.Label20.configure(text='''Username :''')

        # USERNAME ENTRY
        self.Entry9 = tk.Entry(self.Registration)
        self.Entry9.place(x=209, y=342, height=27, width=200)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="black")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(selectbackground="blue")
        self.Entry9.configure(selectforeground="white")

        # PIN LABEL
        self.Label22 = tk.Label(self.Registration)
        self.Label22.place(x=42, y=406, height=39, width=110)
        self.Label22.configure(activebackground="#f9f9f9")
        self.Label22.configure(activeforeground="black")
        self.Label22.configure(background="#ffffff")
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(font="-family {Verdana} -size 11 -weight bold")
        self.Label22.configure(foreground="#000000")
        self.Label22.configure(highlightbackground="#d9d9d9")
        self.Label22.configure(highlightcolor="black")
        self.Label22.configure(text='''Pin :''')

        # PIN ENTRY
        self.Entry10 = tk.Entry(self.Registration)
        self.Entry10.place(x=209, y=416, height=27, width=200)
        self.Entry10.configure(background="white")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(highlightbackground="#d9d9d9")
        self.Entry10.configure(highlightcolor="black")
        self.Entry10.configure(insertbackground="black")
        self.Entry10.configure(selectbackground="blue")
        self.Entry10.configure(selectforeground="white")

        # CONFIRM PIN LABEL
        self.Label22_1 = tk.Label(self.Registration)
        self.Label22_1.place(x=11, y=475, height=39, width=192)
        self.Label22_1.configure(activebackground="#f9f9f9")
        self.Label22_1.configure(activeforeground="black")
        self.Label22_1.configure(background="#ffffff")
        self.Label22_1.configure(disabledforeground="#a3a3a3")
        self.Label22_1.configure(font="-family {Verdana} -size 11 -weight bold")
        self.Label22_1.configure(foreground="#000000")
        self.Label22_1.configure(highlightbackground="#d9d9d9")
        self.Label22_1.configure(highlightcolor="black")
        self.Label22_1.configure(text='''Confirm pin :''')

        # CONFIRM PIN ENTRY
        self.Entry10_1 = tk.Entry(self.Registration)
        self.Entry10_1.place(x=209, y=481, height=27, width=200)
        self.Entry10_1.configure(background="white")
        self.Entry10_1.configure(disabledforeground="#a3a3a3")
        self.Entry10_1.configure(font="TkFixedFont")
        self.Entry10_1.configure(foreground="#000000")
        self.Entry10_1.configure(highlightbackground="#d9d9d9")
        self.Entry10_1.configure(highlightcolor="black")
        self.Entry10_1.configure(insertbackground="black")
        self.Entry10_1.configure(selectbackground="blue")
        self.Entry10_1.configure(selectforeground="white")

        # REGISTER BUTTON
        self.Button7 = tk.Button(self.Registration, command=lambda: self.validation_thread(None))
        self.Button7.place(x=198, y=565, height=34, width=155)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#000000")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font="-family {Verdana} -size 10 -weight bold")
        self.Button7.configure(foreground="#e8e800")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Register''')

        # ------------------Overview Frame-----------------------
        self.overviewframe = tk.Frame(top)
        self.overviewframe.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.overviewframe.configure(relief='groove')
        self.overviewframe.configure(borderwidth="2")
        self.overviewframe.configure(background="#ffffff")
        self.overviewframe.configure(highlightbackground="#d9d9d9")
        self.overviewframe.configure(highlightcolor="black")

        # USER ACCOUNT NUMBER LABEL
        self.active = tk.Label(self.overviewframe)
        self.active.place(relx=0.018, rely=0.088, height=39, width=135)
        self.active.configure(activebackground="#f9f9f9")
        self.active.configure(activeforeground="black")
        self.active.configure(background="#ffffff")
        self.active.configure(disabledforeground="#a3a3a3")
        self.active.configure(font="-family {Verdana} -size 12 -weight bold")
        self.active.configure(foreground="#000000")
        self.active.configure(highlightbackground="#d9d9d9")
        self.active.configure(highlightcolor="black")
        # self.cursor.execute("SELECT Acc_num from reg_bank where username = '{}".format(username))
        # self.active.configure(text='''...........''')

        # HORIZONTAL LINE
        self.TSeparator1 = ttk.Separator(self.overviewframe)
        self.TSeparator1.place(relx=0.051, rely=-2.0, relwidth=0.954)

        # USER FULLNAME LABEL
        self.name = tk.Label(self.overviewframe)
        self.name.place(relx=-0.06, rely=0.191, height=39, width=196)
        self.name.configure(activebackground="#f9f9f9")
        self.name.configure(activeforeground="black")
        self.name.configure(background="#ffffff")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="-family {Verdana} -size 11 -weight bold")
        self.name.configure(foreground="#000000")
        self.name.configure(justify='left')
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="black")
        # self.name.configure(text='hehehe')

        # ACCOUNT BALANCE LABEL
        self.balance = tk.Label(self.overviewframe)
        self.balance.place(relx=0.018, rely=0.144, height=40, width=93)
        self.balance.configure(activebackground="#f9f9f9")
        self.balance.configure(activeforeground="black")
        self.balance.configure(background="#ffffff")
        self.balance.configure(disabledforeground="#a3a3a3")
        self.balance.configure(font="-family {Verdana} -size 12 -weight bold")
        self.balance.configure(foreground="#000000")
        self.balance.configure(highlightbackground="#d9d9d9")
        self.balance.configure(highlightcolor="black")
        self.balance.configure(text='''********''')

        # SHOW BALANCE BUTTON
        self.shwbalance = tk.Button(self.overviewframe, command=self.show_balance)
        self.shwbalance.place(relx=0.752, rely=0.186, height=34, width=107)
        self.shwbalance.configure(activebackground="#ececec")
        self.shwbalance.configure(activeforeground="#000000")
        self.shwbalance.configure(background="#ffffff")
        self.shwbalance.configure(cursor="arrow")
        self.shwbalance.configure(disabledforeground="#a3a3a3")
        self.shwbalance.configure(font="-family {Verdana} -size 9 -weight bold")
        self.shwbalance.configure(foreground="#000000")
        self.shwbalance.configure(highlightbackground="#d9d9d9")
        self.shwbalance.configure(highlightcolor="black")
        self.shwbalance.configure(pady="0")
        self.shwbalance.configure(relief="groove")
        self.shwbalance.configure(text='''Show Balance''')

        # EASYLINK LABEL
        self.easylink = tk.Label(self.overviewframe)
        self.easylink.place(relx=0.034, rely=0.256, height=21, width=63)
        self.easylink.configure(activebackground="#f9f9f9")
        self.easylink.configure(activeforeground="black")
        self.easylink.configure(background="#ffffff")
        self.easylink.configure(disabledforeground="#a3a3a3")
        self.easylink.configure(font="-family {Verdana} -size 10 -weight bold")
        self.easylink.configure(foreground="#000000")
        self.easylink.configure(highlightbackground="#d9d9d9")
        self.easylink.configure(highlightcolor="black")
        self.easylink.configure(text='''Easylink''')
        
        # HORIZONTAL LINE
        self.TSeparator1_1 = ttk.Separator(self.overviewframe)
        self.TSeparator1_1.place(relx=0.019, rely=0.321, relwidth=0.954)

        # OVERVIEW BUTTON
        self.overviewbutton = tk.Button(self.overviewframe)
        self.overviewbutton.place(relx=0.068, rely=0.419, height=40, width=107)
        self.overviewbutton.configure(activebackground="#ececec")
        self.overviewbutton.configure(activeforeground="#000000")
        self.overviewbutton.configure(background="#000000")
        self.overviewbutton.configure(disabledforeground="#a3a3a3")
        self.overviewbutton.configure(foreground="#e8e800")
        self.overviewbutton.configure(highlightbackground="#d9d9d9")
        self.overviewbutton.configure(highlightcolor="black")
        self.overviewbutton.configure(pady="0")
        self.overviewbutton.config()
        self.overviewbutton.configure(relief="sunken")
        self.overviewbutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.overviewbutton.configure(text='''Overview''')

        # AIRTIME BUTTON
        self.airtimebutton = tk.Button(self.overviewframe, command=lambda: self.show_frame(self.airtime))
        self.airtimebutton.place(relx=0.407, rely=0.419, height=40, width=107)
        self.airtimebutton.configure(activebackground="#ececec")
        self.airtimebutton.configure(activeforeground="#000000")
        self.airtimebutton.configure(background="#000000")
        self.airtimebutton.configure(disabledforeground="#a3a3a3")
        self.airtimebutton.configure(foreground="#e8e800")
        self.airtimebutton.configure(highlightbackground="#d9d9d9")
        self.airtimebutton.configure(highlightcolor="black")
        self.airtimebutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.airtimebutton.configure(pady="0")
        self.airtimebutton.configure(relief="groove")
        self.airtimebutton.configure(text='''Airtime''')

        # TRANSFER BUTTON
        self.Transferbutton = tk.Button(self.overviewframe, command=lambda: self.show_frame(self.transfer))
        self.Transferbutton.place(relx=0.727, rely=0.419, height=40, width=107)
        self.Transferbutton.configure(activebackground="#ececec")
        self.Transferbutton.configure(activeforeground="#000000")
        self.Transferbutton.configure(background="#000000")
        self.Transferbutton.configure(disabledforeground="#a3a3a3")
        self.Transferbutton.configure(foreground="#e8e800")
        self.Transferbutton.configure(highlightbackground="#d9d9d9")
        self.Transferbutton.configure(highlightcolor="black")
        self.Transferbutton.configure(pady="0")
        self.Transferbutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Transferbutton.configure(relief="groove")
        self.Transferbutton.configure(text='''Transfer''')

        # BILLS BUTTON
        self.Billsbutton = tk.Button(self.overviewframe, command=lambda: self.show_frame(self.bills))
        self.Billsbutton.place(relx=0.068, rely=0.619, height=40, width=107)
        self.Billsbutton.configure(activebackground="#ececec")
        self.Billsbutton.configure(activeforeground="#000000")
        self.Billsbutton.configure(background="#000000")
        self.Billsbutton.configure(disabledforeground="#a3a3a3")
        self.Billsbutton.configure(foreground="#e8e800")
        self.Billsbutton.configure(highlightbackground="#d9d9d9")
        self.Billsbutton.configure(highlightcolor="black")
        self.Billsbutton.configure(pady="0")
        self.Billsbutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Billsbutton.configure(relief="groove")
        self.Billsbutton.configure(text='''Bills''')

        # EXCHANGE BUTTON
        self.Exchange = tk.Button(self.overviewframe, command=lambda: self.show_frame(self.exchange))
        self.Exchange.place(relx=0.407, rely=0.619, height=40, width=107)
        self.Exchange.configure(activebackground="#f9f9f9")
        self.Exchange.configure(activeforeground="#000000")
        self.Exchange.configure(background="#000000")
        self.Exchange.configure(cursor="arrow")
        self.Exchange.configure(disabledforeground="#a3a3a3")
        self.Exchange.configure(font="-family {Segoe UI} -size 9")
        self.Exchange.configure(foreground="#e8e800")
        self.Exchange.configure(highlightbackground="#d9d9d9")
        self.Exchange.configure(highlightcolor="black")
        self.Exchange.configure(pady="0")
        self.Exchange.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Exchange.configure(relief="groove")
        self.Exchange.configure(text='''Exchange''')

        # SETTINGS BUTTON
        self.Settingsbutton = tk.Button(self.overviewframe, command=lambda: self.show_frame(self.Settingsframe))
        self.Settingsbutton.place(relx=0.727, rely=0.619, height=40, width=107)
        self.Settingsbutton.configure(activebackground="#ececec")
        self.Settingsbutton.configure(activeforeground="#000000")
        self.Settingsbutton.configure(background="#000000")
        self.Settingsbutton.configure(disabledforeground="#a3a3a3")
        self.Settingsbutton.configure(foreground="#e8e800")
        self.Settingsbutton.configure(highlightbackground="#d9d9d9")
        self.Settingsbutton.configure(highlightcolor="black")
        self.Settingsbutton.configure(pady="0")
        self.Settingsbutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Settingsbutton.configure(relief="groove")
        self.Settingsbutton.configure(text='''Settings''')

        # ---------------Airtime Page--------------
        self.airtime = tk.Frame(top)
        self.airtime.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.airtime.configure(relief='groove')
        self.airtime.configure(borderwidth="2")
        self.airtime.configure(relief="groove")
        self.airtime.configure(background="#ffffff")
        self.airtime.configure(cursor="arrow")
        self.airtime.configure(highlightbackground="#d9d9d9")
        self.airtime.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.airtime)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=145)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img9
        # _img9 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img9)
        self.Label1.configure(text='''Label''')

        # AIRTIME LABELFRAME
        self.airtimelabelframe = tk.LabelFrame(self.airtime)
        self.airtimelabelframe.place(relx=0.105, rely=0.190, relheight=0.709, relwidth=0.795)
        self.airtimelabelframe.configure(relief='groove')
        self.airtimelabelframe.configure(font="-family {Verdana} -size 10 -weight bold")
        self.airtimelabelframe.configure(foreground="black")
        self.airtimelabelframe.configure(text='''Airtime''')
        self.airtimelabelframe.configure(background="#ffffff")
        self.airtimelabelframe.configure(highlightbackground="#d9d9d9")
        self.airtimelabelframe.configure(highlightcolor="black")

        # SELECT MOBILE OPERATOR LABEL
        self.SMOlabel = tk.Label(self.airtimelabelframe)
        self.SMOlabel.place(relx=0.018, rely=0.058, height=41, width=179, bordermode='ignore')
        self.SMOlabel.configure(activebackground="#f9f9f9")
        self.SMOlabel.configure(activeforeground="black")
        self.SMOlabel.configure(background="#ffffff")
        self.SMOlabel.configure(disabledforeground="#a3a3a3")
        self.SMOlabel.configure(font="-family {Verdana} -size 9 -weight bold")
        self.SMOlabel.configure(foreground="#000000")
        self.SMOlabel.configure(highlightbackground="#d9d9d9")
        self.SMOlabel.configure(highlightcolor="black")
        self.SMOlabel.configure(text='''Select Mobile Operator''')

        # AIRTEL BUTTON
        self.airtelbutton = tk.Button(self.airtimelabelframe, command=self.active_airtelbutton)
        self.airtelbutton.place(relx=0.240, rely=0.174, height=42, width=77, bordermode='ignore')
        self.airtelbutton.configure(activebackground="#ececec")
        self.airtelbutton.configure(activeforeground="#000000")
        self.airtelbutton.configure(background="#ff0000")
        self.airtelbutton.configure(cursor="arrow")
        self.airtelbutton.configure(disabledforeground="#a3a3a3")
        self.airtelbutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.airtelbutton.configure(foreground="#ffffff")
        self.airtelbutton.configure(highlightbackground="#d9d9d9")
        self.airtelbutton.configure(highlightcolor="black")
        self.airtelbutton.configure(pady="0")
        self.airtelbutton.configure(relief="groove")
        self.airtelbutton.configure(text='''Airtel''')

        # 9 MOBILE BUTTON
        self.vmobilebuuton = tk.Button(self.airtimelabelframe, command=self.active_vmobilebutton)
        self.vmobilebuuton.place(relx=0.039, rely=0.174, height=42, width=77, bordermode='ignore')
        self.vmobilebuuton.configure(activebackground="#ececec")
        self.vmobilebuuton.configure(activeforeground="#000000")
        self.vmobilebuuton.configure(background="#000000")
        self.vmobilebuuton.configure(cursor="arrow")
        self.vmobilebuuton.configure(disabledforeground="#a3a3a3")
        self.vmobilebuuton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.vmobilebuuton.configure(foreground="#3faf38")
        self.vmobilebuuton.configure(highlightbackground="#d9d9d9")
        self.vmobilebuuton.configure(highlightcolor="black")
        self.vmobilebuuton.configure(pady="0")
        self.vmobilebuuton.configure(relief="groove")
        self.vmobilebuuton.configure(text='''9Mobile''')

        # MTN BUTTON
        self.mtnbutton = tk.Button(self.airtimelabelframe, command=self.active_mtnbutton)
        self.mtnbutton.place(relx=0.420, rely=0.174, height=42, width=77, bordermode='ignore')
        self.mtnbutton.configure(activebackground="#ececec")
        self.mtnbutton.configure(activeforeground="#000000")
        self.mtnbutton.configure(background="#e6e600")
        self.mtnbutton.configure(cursor="arrow")
        self.mtnbutton.configure(disabledforeground="#a3a3a3")
        self.mtnbutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.mtnbutton.configure(foreground="#000000")
        self.mtnbutton.configure(highlightbackground="#d9d9d9")
        self.mtnbutton.configure(highlightcolor="black")
        self.mtnbutton.configure(pady="0")
        self.mtnbutton.configure(relief="groove")
        self.mtnbutton.configure(text='''MTN''')

        # GLO BUTTON
        self.globutton = tk.Button(self.airtimelabelframe, command=self.active_globutton)
        self.globutton.place(relx=0.620, rely=0.174, height=42, width=77, bordermode='ignore')
        self.globutton.configure(activebackground="#ececec")
        self.globutton.configure(activeforeground="#000000")
        self.globutton.configure(background="#00cc00")
        self.globutton.configure(cursor="arrow")
        self.globutton.configure(disabledforeground="#a3a3a3")
        self.globutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.globutton.configure(foreground="#ffffff")
        self.globutton.configure(highlightbackground="#d9d9d9")
        self.globutton.configure(highlightcolor="black")
        self.globutton.configure(pady="0")
        self.globutton.configure(relief="groove")
        self.globutton.configure(text='''Glo''')

        # MOBILE NUMBER BUTTON
        self.mnumlabel = tk.Label(self.airtimelabelframe)
        self.mnumlabel.place(relx=0.018, rely=0.348, height=31, width=118, bordermode='ignore')
        self.mnumlabel.configure(activebackground="#f9f9f9")
        self.mnumlabel.configure(activeforeground="black")
        self.mnumlabel.configure(background="#ffffff")
        self.mnumlabel.configure(cursor="arrow")
        self.mnumlabel.configure(disabledforeground="#a3a3a3")
        self.mnumlabel.configure(font="-family {Verdana} -size 9 -weight bold")
        self.mnumlabel.configure(foreground="#000000")
        self.mnumlabel.configure(highlightbackground="#d9d9d9")
        self.mnumlabel.configure(highlightcolor="black")
        self.mnumlabel.configure(text='''Mobile Number''')

        # MOBILE NUMBER ENTRY
        self.mnumentry = tk.Entry(self.airtimelabelframe)
        self.mnumentry.place(relx=0.039, rely=0.435, height=30, relwidth=0.411, bordermode='ignore')
        self.mnumentry.configure(background="white")
        self.mnumentry.configure(cursor="arrow")
        self.mnumentry.configure(disabledforeground="#a3a3a3")
        self.mnumentry.configure(font="-family {Verdana} -size 9 -weight bold")
        self.mnumentry.configure(foreground="#000000")
        self.mnumentry.configure(highlightbackground="#d9d9d9")
        self.mnumentry.configure(highlightcolor="black")
        self.mnumentry.configure(insertbackground="black")
        self.mnumentry.configure(relief="groove")
        self.mnumentry.configure(selectbackground="blue")
        self.mnumentry.configure(selectforeground="white")

        # HORIZONTAL LINE
        self.TSeparator2 = ttk.Separator(self.airtimelabelframe)
        self.TSeparator2.place(relx=0.042, rely=0.548, relwidth=0.886, bordermode='ignore')
        self.TSeparator2.configure(cursor="arrow")

        # AMOUNT LABEL
        self.amountlabel = tk.Label(self.airtimelabelframe)
        self.amountlabel.place(relx=0.018, rely=0.58, height=21, width=77, bordermode='ignore')
        self.amountlabel.configure(activebackground="#f9f9f9")
        self.amountlabel.configure(activeforeground="black")
        self.amountlabel.configure(background="#ffffff")
        self.amountlabel.configure(cursor="arrow")
        self.amountlabel.configure(disabledforeground="#a3a3a3")
        self.amountlabel.configure(font="-family {Verdana} -size 9 -weight bold")
        self.amountlabel.configure(foreground="#000000")
        self.amountlabel.configure(highlightbackground="#d9d9d9")
        self.amountlabel.configure(highlightcolor="black")
        self.amountlabel.configure(text='''Amount''')

        # AMOUNT ENTRY
        self.amountentry = tk.Entry(self.airtimelabelframe)
        self.amountentry.place(relx=0.039, rely=0.667, height=30, relwidth=0.411, bordermode='ignore')
        self.amountentry.configure(background="white")
        self.amountentry.configure(cursor="arrow")
        self.amountentry.configure(disabledforeground="#a3a3a3")
        self.amountentry.configure(font="-family {Verdana} -size 9 -weight bold")
        self.amountentry.configure(foreground="#000000")
        self.amountentry.configure(highlightbackground="#ffffff")
        self.amountentry.configure(highlightcolor="black")
        self.amountentry.configure(insertbackground="black")
        self.amountentry.configure(relief="groove")
        self.amountentry.configure(selectbackground="blue")
        self.amountentry.configure(selectforeground="white")

        # HORIZONTAL LINE
        self.TSeparator3 = ttk.Separator(self.airtimelabelframe)
        self.TSeparator3.place(relx=0.042, rely=0.777, relwidth=0.886, bordermode='ignore')

        # SUBMIT BUTTON
        self.submitbutton = tk.Button(self.airtimelabelframe, command=self.airtime_recharge)
        self.submitbutton.place(relx=0.358, rely=0.829, height=35, width=120, bordermode='ignore')
        self.submitbutton.configure(activebackground="#ececec")
        self.submitbutton.configure(activeforeground="#000000")
        self.submitbutton.configure(background="#000000")
        self.submitbutton.configure(cursor="arrow")
        self.submitbutton.configure(disabledforeground="#a3a3a3")
        self.submitbutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.submitbutton.configure(foreground="#e8e800")
        self.submitbutton.configure(highlightbackground="#d9d9d9")
        self.submitbutton.configure(highlightcolor="black")
        self.submitbutton.configure(pady="0")
        self.submitbutton.configure(relief="groove")
        self.submitbutton.configure(text='''Submit''')

        # RETURN TO OVERVIEW BUTTON
        self.return_overview = tk.Button(self.airtime, command=lambda: self.show_frame(self.overviewframe))
        self.return_overview.place(relx=0.786, rely=0.060, height=34, width=105)
        self.return_overview.configure(activebackground="#ececec")
        self.return_overview.configure(activeforeground="#000000")
        self.return_overview.configure(background="#000000")
        self.return_overview.configure(cursor="arrow")
        self.return_overview.configure(disabledforeground="#a3a3a3")
        self.return_overview.configure(font="-family {Verdana} -size 9 -weight bold")
        self.return_overview.configure(foreground="#e8e800")
        self.return_overview.configure(highlightbackground="#d9d9d9")
        self.return_overview.configure(highlightcolor="black")
        self.return_overview.configure(pady="0")
        self.return_overview.configure(relief="groove")
        self.return_overview.configure(text='''Overview''')

        # -------------------TRANSFER PAGE---------------------
        self.transfer = tk.Frame(top)
        self.transfer.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.transfer.configure(relief='groove')
        self.transfer.configure(borderwidth="2")
        self.transfer.configure(relief="groove")
        self.transfer.configure(background="#ffffff")
        self.transfer.configure(highlightbackground="#d9d9d9")
        self.transfer.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.transfer)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=138)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img11
        # _img11 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img11)
        self.Label1.configure(text='''Label''')

        # TRANSFER LABEL FRAME
        self.transfer_frame = tk.LabelFrame(self.transfer)
        self.transfer_frame.place(relx=0.103, rely=0.165, relheight=0.709, relwidth=0.795)
        self.transfer_frame.configure(relief='groove')
        self.transfer_frame.configure(font="-family {Verdana} -size 10 -weight bold")
        self.transfer_frame.configure(foreground="black")
        self.transfer_frame.configure(text='''Transfer''')
        self.transfer_frame.configure(background="#ffffff")
        self.transfer_frame.configure(highlightbackground="#d9d9d9")
        self.transfer_frame.configure(highlightcolor="black")

        # DESTINATION ACCOUNT LABEL
        self.desacct_label = tk.Label(self.transfer_frame)
        self.desacct_label.place(relx=0.018, rely=0.087, height=31, width=149, bordermode='ignore')
        self.desacct_label.configure(activebackground="#f9f9f9")
        self.desacct_label.configure(activeforeground="black")
        self.desacct_label.configure(background="#ffffff")
        self.desacct_label.configure(cursor="arrow")
        self.desacct_label.configure(disabledforeground="#a3a3a3")
        self.desacct_label.configure(font="-family {Verdana} -size 9 -weight bold")
        self.desacct_label.configure(foreground="#000000")
        self.desacct_label.configure(highlightbackground="#d9d9d9")
        self.desacct_label.configure(highlightcolor="black")
        self.desacct_label.configure(text='''Destination Account''')

        # DESTINATION ACCOUNT ENTRY
        self.desacct_entry = tk.Entry(self.transfer_frame)
        self.desacct_entry.place(relx=0.039, rely=0.171, height=30, relwidth=0.411, bordermode='ignore')
        self.desacct_entry.configure(background="white")
        self.desacct_entry.configure(cursor="arrow")
        self.desacct_entry.configure(disabledforeground="#a3a3a3")
        self.desacct_entry.configure(font="-family {Verdana} -size 9 -weight bold")
        self.desacct_entry.configure(foreground="#000000")
        self.desacct_entry.configure(highlightbackground="#d9d9d9")
        self.desacct_entry.configure(highlightcolor="black")
        self.desacct_entry.configure(insertbackground="black")
        self.desacct_entry.configure(relief="groove")
        self.desacct_entry.configure(selectbackground="blue")
        self.desacct_entry.configure(selectforeground="white")

        # HORIZONTAL LINE
        self.TSeparator4 = ttk.Separator(self.transfer_frame)
        self.TSeparator4.place(relx=0.042, rely=0.281, relwidth=0.886, bordermode='ignore')
        self.TSeparator4.configure(cursor="arrow")

        # AMOUNT LABEL
        self.amount_label = tk.Label(self.transfer_frame)
        self.amount_label.place(relx=0.018, rely=0.313, height=30, width=66, bordermode='ignore')
        self.amount_label.configure(activebackground="#f9f9f9")
        self.amount_label.configure(activeforeground="black")
        self.amount_label.configure(background="#ffffff")
        self.amount_label.configure(cursor="arrow")
        self.amount_label.configure(disabledforeground="#a3a3a3")
        self.amount_label.configure(font="-family {Verdana} -size 9 -weight bold")
        self.amount_label.configure(foreground="#000000")
        self.amount_label.configure(highlightbackground="#d9d9d9")
        self.amount_label.configure(highlightcolor="black")
        self.amount_label.configure(text='''Amount''')

        # AMOUNT ENTRY
        self.ammount_entry = tk.Entry(self.transfer_frame)
        self.ammount_entry.place(relx=0.039, rely=0.397, height=30, relwidth=0.411, bordermode='ignore')
        self.ammount_entry.configure(background="white")
        self.ammount_entry.configure(cursor="arrow")
        self.ammount_entry.configure(disabledforeground="#a3a3a3")
        self.ammount_entry.configure(font="-family {Verdana} -size 9 -weight bold")
        self.ammount_entry.configure(foreground="#000000")
        self.ammount_entry.configure(highlightbackground="#d9d9d9")
        self.ammount_entry.configure(highlightcolor="black")
        self.ammount_entry.configure(insertbackground="black")
        self.ammount_entry.configure(relief="groove")
        self.ammount_entry.configure(selectbackground="blue")
        self.ammount_entry.configure(selectforeground="white")

        # HORIZONTAL LINE
        self.TSeparator5 = ttk.Separator(self.transfer_frame)
        self.TSeparator5.place(relx=0.042, rely=0.504, relwidth=0.886, bordermode='ignore')
        self.TSeparator5.configure(cursor="arrow")

        # TRANSACTION DESCRIPTION LABEL
        self.trans_descp_label = tk.Label(self.transfer_frame)
        self.trans_descp_label.place(relx=0.018, rely=0.539, height=30, width=179, bordermode='ignore')
        self.trans_descp_label.configure(activebackground="#f9f9f9")
        self.trans_descp_label.configure(activeforeground="black")
        self.trans_descp_label.configure(background="#ffffff")
        self.trans_descp_label.configure(cursor="arrow")
        self.trans_descp_label.configure(disabledforeground="#a3a3a3")
        self.trans_descp_label.configure(font="-family {Verdana} -size 9 -weight bold")
        self.trans_descp_label.configure(foreground="#000000")
        self.trans_descp_label.configure(highlightbackground="#d9d9d9")
        self.trans_descp_label.configure(highlightcolor="black")
        self.trans_descp_label.configure(text='''Transaction Description''')

        # TRANSACTION DESCRIPTION ENTRY
        self.trans_descp_entry = tk.Entry(self.transfer_frame)
        self.trans_descp_entry.place(relx=0.039, rely=0.623, height=30, relwidth=0.411, bordermode='ignore')
        self.trans_descp_entry.configure(background="white")
        self.trans_descp_entry.configure(cursor="arrow")
        self.trans_descp_entry.configure(disabledforeground="#a3a3a3")
        self.trans_descp_entry.configure(font="-family {Verdana} -size 9 -weight bold")
        self.trans_descp_entry.configure(foreground="#000000")
        self.trans_descp_entry.configure(highlightbackground="#d9d9d9")
        self.trans_descp_entry.configure(highlightcolor="black")
        self.trans_descp_entry.configure(insertbackground="black")
        self.trans_descp_entry.configure(relief="groove")
        self.trans_descp_entry.configure(selectbackground="blue")
        self.trans_descp_entry.configure(selectforeground="white")

        # HORIZONTAL LINE
        self.TSeparator6 = ttk.Separator(self.transfer_frame)
        self.TSeparator6.place(relx=0.042, rely=0.733, relwidth=0.886, bordermode='ignore')

        # CONTINUE(SUBMIT) BUTTON
        self.transfer_submit_button = tk.Button(self.transfer_frame, command=lambda: self.transfering_thread(None))
        self.transfer_submit_button.place(relx=0.358, rely=0.829, height=35, width=120, bordermode='ignore')
        self.transfer_submit_button.configure(activebackground="#ececec")
        self.transfer_submit_button.configure(activeforeground="#000000")
        self.transfer_submit_button.configure(background="#000000")
        self.transfer_submit_button.configure(disabledforeground="#a3a3a3")
        self.transfer_submit_button.configure(font="-family {Verdana} -size 9 -weight bold")
        self.transfer_submit_button.configure(foreground="#e8e800")
        self.transfer_submit_button.configure(highlightbackground="#d9d9d9")
        self.transfer_submit_button.configure(highlightcolor="black")
        self.transfer_submit_button.configure(pady="0")
        self.transfer_submit_button.configure(relief="groove")
        self.transfer_submit_button.configure(text='''Continue''')

        # RETURN TO OVERVIEW BUTTON
        self.Button1 = tk.Button(self.transfer, command=lambda: self.show_frame(self.overviewframe))
        self.Button1.place(relx=0.786, rely=0.060, height=34, width=105)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#000000")
        self.Button1.configure(cursor="arrow")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        self.Button1.configure(foreground="#e8e800")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''Overview''')


        # ------------------BILLS PAGE------------------
        self.bills = tk.Frame(top)
        self.bills.place(relx=0.017, rely=0.022, relheight=0.935, relwidth=0.975)
        self.bills.configure(relief='groove')
        self.bills.configure(borderwidth="2")
        self.bills.configure(relief="groove")
        self.bills.configure(background="#ffffff")
        self.bills.configure(highlightbackground="#d9d9d9")
        self.bills.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.bills)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=138)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img12
        # _img12 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img12)
        self.Label1.configure(text='''Label''')

        # BACK TO OVERVIEW BUTTON
        self.billsreturn_overview = tk.Button(self.bills, command=lambda: self.show_frame(self.overviewframe))
        self.billsreturn_overview.place(relx=0.786, rely=0.060, height=34, width=105)
        self.billsreturn_overview.configure(activebackground="#ececec")
        self.billsreturn_overview.configure(activeforeground="#000000")
        self.billsreturn_overview.configure(background="#ffffff")
        self.billsreturn_overview.configure(disabledforeground="#a3a3a3")
        self.billsreturn_overview.configure(font="-family {Segoe UI} -size 9")
        self.billsreturn_overview.configure(foreground="#000000")
        self.billsreturn_overview.configure(highlightbackground="#d9d9d9")
        self.billsreturn_overview.configure(highlightcolor="black")
        self.billsreturn_overview.configure(pady="0")
        self.billsreturn_overview.configure(relief="groove")
        self.billsreturn_overview.configure(text='''Overview''')

        # BILLS LABELFRAME
        self.bills_label_frame = tk.LabelFrame(self.bills)
        self.bills_label_frame.place(relx=0.103, rely=0.163, relheight=0.709, relwidth=0.795)
        self.bills_label_frame.configure(relief='groove')
        self.bills_label_frame.configure(font="-family {Verdana} -size 10 -weight bold")
        self.bills_label_frame.configure(foreground="black")
        self.bills_label_frame.configure(text='''Bills''')
        self.bills_label_frame.configure(background="#ffffff")
        self.bills_label_frame.configure(cursor="arrow")
        self.bills_label_frame.configure(highlightbackground="#d9d9d9")
        self.bills_label_frame.configure(highlightcolor="black")

        # SELECT CATEGORY LABEL
        self.Label1 = tk.Label(self.bills_label_frame)
        self.Label1.place(relx=0.022, rely=0.066, height=27, width=149, bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Select Category''')

        # COMBO BOX - DROPDOWN
        self.com46 = tk.StringVar()
        self.TCombobox1 = ttk.Combobox(self.bills_label_frame)
        self.TCombobox1.place(relx=0.065, rely=0.164, relheight=0.098, relwidth=0.482, bordermode='ignore')
        self.TCombobox1.configure(font="-family {Verdana} -size 9 -weight bold")
        self.TCombobox1.configure(textvariable=self.com46)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1 ['values'] = ('Airlines', 'Cable TV', 'Electricity', 'Insurance', 'Investement','Schools', 'Taxes')
        # self.TCombobox1.grid(crelx)
        self.TCombobox1.current()

        # AMOUNT LABEL
        self.Bills_Label3 = tk.Label(self.bills_label_frame)
        self.Bills_Label3.place(relx=0.022, rely=0.597, height=27, width=149, bordermode='ignore')
        self.Bills_Label3.configure(activebackground="#f9f9f9")
        self.Bills_Label3.configure(activeforeground="black")
        self.Bills_Label3.configure(background="#ffffff")
        self.Bills_Label3.configure(disabledforeground="#a3a3a3")
        self.Bills_Label3.configure(font="-family {Verdana} -size 10 -weight bold")
        self.Bills_Label3.configure(foreground="#000000")
        self.Bills_Label3.configure(highlightbackground="#d9d9d9")
        self.Bills_Label3.configure(highlightcolor="black")
        self.Bills_Label3.configure(text='''Amount :''')

        # AMOUNT ENTRY
        self.bills_entry = tk.Entry(self.bills_label_frame)
        self.bills_entry.place(relx=0.279, rely=0.597, height=30, width=141, bordermode='ignore')
        self.bills_entry.configure(background="white")
        self.bills_entry.configure(cursor="arrow")
        self.bills_entry.configure(disabledforeground="#a3a3a3")
        self.bills_entry.configure(font="-family {Verdana} -size 9 -weight bold")
        self.bills_entry.configure(foreground="#000000")
        self.bills_entry.configure(highlightbackground="#d9d9d9")
        self.bills_entry.configure(highlightcolor="black")
        self.bills_entry.configure(insertbackground="black")
        self.bills_entry.configure(relief="groove")
        self.bills_entry.configure(selectbackground="blue")
        self.bills_entry.configure(selectforeground="white")

        # CONTINUE (SUBMIT) BUTTON
        self.Bills_Button = tk.Button(self.bills_label_frame, command=lambda: self.show_frame(self.overviewframe))
        self.Bills_Button.place(relx=0.358, rely=0.829, height=35, width=120, bordermode='ignore')
        self.Bills_Button.configure(activebackground="#ececec")
        self.Bills_Button.configure(activeforeground="#000000")
        self.Bills_Button.configure(background="#000000")
        self.Bills_Button.configure(cursor="arrow")
        self.Bills_Button.configure(disabledforeground="#a3a3a3")
        self.Bills_Button.configure(font="-family {Segoe UI} -size 9")
        self.Bills_Button.configure(foreground="#e8e800")
        self.Bills_Button.configure(highlightbackground="#d9d9d9")
        self.Bills_Button.configure(highlightcolor="black")
        self.Bills_Button.configure(pady="0")
        self.Bills_Button.configure(relief="groove")
        self.Bills_Button.configure(text='''Continue''')

        # -------------------EXCHANGE PAGE---------------
        self.exchange = tk.Frame(top)
        self.exchange.place(relx=0.017, rely=0.022, relheight=0.935, relwidth=0.975)
        self.exchange.configure(relief='groove')
        self.exchange.configure(borderwidth="2")
        self.exchange.configure(relief="groove")
        self.exchange.configure(background="#ffffff")
        self.exchange.configure(highlightbackground="#d9d9d9")
        self.exchange.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.exchange)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=138)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img17
        # _img17 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img17)
        self.Label1.configure(text='''Label''')

        # RETURN TO OVERVIEW BUTTON
        self.exchangereturn_overview = tk.Button(self.exchange, command=lambda: self.show_frame(self.overviewframe))
        self.exchangereturn_overview.place(relx=0.786, rely=0.060, height=34, width=105)
        self.exchangereturn_overview.configure(activebackground="#ececec")
        self.exchangereturn_overview.configure(activeforeground="#000000")
        self.exchangereturn_overview.configure(background="#000000")
        self.exchangereturn_overview.configure(cursor="arrow")
        self.exchangereturn_overview.configure(disabledforeground="#a3a3a3")
        self.exchangereturn_overview.configure(font="-family {Verdana} -size 9 -weight bold")
        self.exchangereturn_overview.configure(foreground="#e8e800")
        self.exchangereturn_overview.configure(highlightbackground="#d9d9d9")
        self.exchangereturn_overview.configure(highlightcolor="black")
        self.exchangereturn_overview.configure(pady="0")
        self.exchangereturn_overview.configure(relief="groove")
        self.exchangereturn_overview.configure(text='''Overview''')

        # EXCHANGE LABELFRAME
        self.exchange_frame = tk.LabelFrame(self.exchange)
        self.exchange_frame.place(relx=0.103, rely=0.165, relheight=0.709, relwidth=0.795)
        self.exchange_frame.configure(relief='groove')
        self.exchange_frame.configure(font="-family {Verdana} -size 10 -weight bold")
        self.exchange_frame.configure(foreground="black")
        self.exchange_frame.configure(text='''Exchange''')
        self.exchange_frame.configure(background="#ffffff")
        self.exchange_frame.configure(highlightbackground="#d9d9d9")
        self.exchange_frame.configure(highlightcolor="black")

        # DESTINATION ACCOUNT LABEL
        self.desacct_label = tk.Label(self.exchange_frame)
        self.desacct_label.place(relx=0.018, rely=0.087, height=31, width=149, bordermode='ignore')
        self.desacct_label.configure(activebackground="#f9f9f9")
        self.desacct_label.configure(activeforeground="black")
        self.desacct_label.configure(background="#ffffff")
        self.desacct_label.configure(cursor="arrow")
        self.desacct_label.configure(disabledforeground="#a3a3a3")
        self.desacct_label.configure(font="-family {Verdana} -size 9 -weight bold")
        self.desacct_label.configure(foreground="#000000")
        self.desacct_label.configure(highlightbackground="#d9d9d9")
        self.desacct_label.configure(highlightcolor="black")
        self.desacct_label.configure(text='''Destination Account''')

        # COMBO BOX - DROPDOWN
        self.com49 = tk.StringVar()
        self.exchangecombo = ttk.Combobox(self.exchange_frame)
        self.exchangecombo.place(relx=0.065, rely=0.164, relheight=0.098, relwidth=0.482, bordermode='ignore')
        self.exchangecombo.configure(textvariable=self.com49)
        self.exchangecombo.configure(takefocus="")
        self.exchangecombo ['values'] = ('USD', 'GBP', 'EUROS', 'CAD', 'YEN')
        self.exchangecombo.current()

        # HORIZONTAL LINE
        self.TSeparator4 = ttk.Separator(self.exchange_frame)
        self.TSeparator4.place(relx=0.042, rely=0.281, relwidth=0.886, bordermode='ignore')
        self.TSeparator4.configure(cursor="arrow")

        # EXCHANGE AMOUNT LABEL
        self.exchange_amount_label = tk.Label(self.exchange_frame)
        self.exchange_amount_label.place(relx=0.018, rely=0.313, height=30, width=66, bordermode='ignore')
        self.exchange_amount_label.configure(activebackground="#f9f9f9")
        self.exchange_amount_label.configure(activeforeground="black")
        self.exchange_amount_label.configure(background="#ffffff")
        self.exchange_amount_label.configure(cursor="arrow")
        self.exchange_amount_label.configure(disabledforeground="#a3a3a3")
        self.exchange_amount_label.configure(font="-family {Verdana} -size 9 -weight bold")
        self.exchange_amount_label.configure(foreground="#000000")
        self.exchange_amount_label.configure(highlightbackground="#d9d9d9")
        self.exchange_amount_label.configure(highlightcolor="black")
        self.exchange_amount_label.configure(text='''Amount''')

        # EXCHANGE AMOUNT ENTRY
        self.exchange_amount_entry = tk.Entry(self.exchange_frame)
        self.exchange_amount_entry.place(relx=0.039, rely=0.397, height=30, relwidth=0.411, bordermode='ignore')
        self.exchange_amount_entry.configure(background="white")
        self.exchange_amount_entry.configure(cursor="arrow")
        self.exchange_amount_entry.configure(disabledforeground="#a3a3a3")
        self.exchange_amount_entry.configure(font="-family {Verdana} -size 9 -weight bold")
        self.exchange_amount_entry.configure(foreground="#000000")
        self.exchange_amount_entry.configure(highlightbackground="#d9d9d9")
        self.exchange_amount_entry.configure(highlightcolor="black")
        self.exchange_amount_entry.configure(insertbackground="black")
        self.exchange_amount_entry.configure(relief="groove")
        self.exchange_amount_entry.configure(selectbackground="blue")
        self.exchange_amount_entry.configure(selectforeground="white")

        # HORIZONTAL LINE
        self.TSeparator5 = ttk.Separator(self.exchange_frame)
        self.TSeparator5.place(relx=0.042, rely=0.504, relwidth=0.886, bordermode='ignore')
        self.TSeparator5.configure(cursor="arrow")

        # TRANSACTION DESCRIPTION LABEL
        self.exchange_descp_label = tk.Label(self.exchange_frame)
        self.exchange_descp_label.place(relx=0.018, rely=0.539, height=30, width=179, bordermode='ignore')
        self.exchange_descp_label.configure(activebackground="#f9f9f9")
        self.exchange_descp_label.configure(activeforeground="black")
        self.exchange_descp_label.configure(background="#ffffff")
        self.exchange_descp_label.configure(cursor="arrow")
        self.exchange_descp_label.configure(disabledforeground="#a3a3a3")
        self.exchange_descp_label.configure(font="-family {Verdana} -size 9 -weight bold")
        self.exchange_descp_label.configure(foreground="#000000")
        self.exchange_descp_label.configure(highlightbackground="#d9d9d9")
        self.exchange_descp_label.configure(highlightcolor="black")
        self.exchange_descp_label.configure(text='''Transaction Description''')

        # TRANSACTION DESCRIPTION ENTRY
        self.exchange_descp_entry = tk.Entry(self.exchange_frame)
        self.exchange_descp_entry.place(relx=0.039, rely=0.623, height=30, relwidth=0.411, bordermode='ignore')
        self.exchange_descp_entry.configure(background="white")
        self.exchange_descp_entry.configure(cursor="arrow")
        self.exchange_descp_entry.configure(disabledforeground="#a3a3a3")
        self.exchange_descp_entry.configure(font="-family {Verdana} -size 9 -weight bold")
        self.exchange_descp_entry.configure(foreground="#000000")
        self.exchange_descp_entry.configure(highlightbackground="#d9d9d9")
        self.exchange_descp_entry.configure(highlightcolor="black")
        self.exchange_descp_entry.configure(insertbackground="black")
        self.exchange_descp_entry.configure(relief="groove")
        self.exchange_descp_entry.configure(selectbackground="blue")
        self.exchange_descp_entry.configure(selectforeground="white")

        # HORIZONTAL LINE
        self.TSeparator6 = ttk.Separator(self.exchange_frame)
        self.TSeparator6.place(relx=0.042, rely=0.733, relwidth=0.886, bordermode='ignore')

        # CONTINUE (SUBMIT) BUTTON
        self.exchange_submit_button = tk.Button(self.exchange_frame)
        self.exchange_submit_button.place(relx=0.358, rely=0.829, height=35, width=120, bordermode='ignore')
        self.exchange_submit_button.configure(activebackground="#ececec")
        self.exchange_submit_button.configure(activeforeground="#000000")
        self.exchange_submit_button.configure(background="#000000")
        self.exchange_submit_button.configure(disabledforeground="#a3a3a3")
        self.exchange_submit_button.configure(font="-family {Verdana} -size 9 -weight bold")
        self.exchange_submit_button.configure(foreground="#e8e800")
        self.exchange_submit_button.configure(highlightbackground="#d9d9d9")
        self.exchange_submit_button.configure(highlightcolor="black")
        self.exchange_submit_button.configure(pady="0")
        self.exchange_submit_button.configure(relief="groove")
        self.exchange_submit_button.configure(text='''Continue''')


        # ----------------------SETTINGS-------------------------------------
        self.Settingsframe = tk.Frame(top)
        self.Settingsframe.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.Settingsframe.configure(relief='groove')
        self.Settingsframe.configure(borderwidth="2")
        self.Settingsframe.configure(relief="groove")
        self.Settingsframe.configure(background="#ffffff")
        self.Settingsframe.configure(highlightbackground="#d9d9d9")
        self.Settingsframe.configure(highlightcolor="black")

        # RETURN OVERVIEW BUTTON
        self.return_overview = tk.Button( self.Settingsframe, command=lambda: self.show_frame(self.overviewframe))
        self.return_overview.place(relx=0.786, rely=0.060, height=34, width=105)
        self.return_overview.configure(activebackground="#ececec")
        self.return_overview.configure(activeforeground="#000000")
        self.return_overview.configure(background="#000000")
        self.return_overview.configure(cursor="arrow")
        self.return_overview.configure(disabledforeground="#a3a3a3")
        self.return_overview.configure(font="-family {Verdana} -size 9 -weight bold")
        self.return_overview.configure(foreground="#e8e800")
        self.return_overview.configure(highlightbackground="#d9d9d9")
        self.return_overview.configure(highlightcolor="black")
        self.return_overview.configure(pady="0")
        self.return_overview.configure(relief="groove")
        self.return_overview.configure(text='''Overview''')

        # CONTACT US BUTTON
        self.contact = tk.Button(self.Settingsframe, command=lambda: self.show_frame(self.connect))
        self.contact.place(relx=0.068, rely=0.628, height=40, width=87)
        self.contact.configure(activebackground="#ececec")
        self.contact.configure(activeforeground="#000000")
        self.contact.configure(background="#000000")
        self.contact.configure(cursor="arrow")
        self.contact.configure(disabledforeground="#a3a3a3")
        self.contact.configure(foreground="#e8e800")
        self.contact.configure(highlightbackground="#d9d9d9")
        self.contact.configure(highlightcolor="black")
        self.contact.configure(pady="0")
        self.contact.configure(font="-family {Verdana} -size 9 -weight bold")
        self.contact.configure(relief="groove")
        self.contact.configure(text='''Contact Us''')

        # CHANGE USERNAME BUTTON
        self.vtubutton = tk.Button(self.Settingsframe, command=lambda: self.show_frame(self.changename))
        self.vtubutton.place(relx=0.308, rely=0.628, height=40, width=97)
        self.vtubutton.configure(activebackground="#ececec")
        self.vtubutton.configure(activeforeground="#000000")
        self.vtubutton.configure(background="#000000")
        self.vtubutton.configure(disabledforeground="#a3a3a3")
        self.vtubutton.configure(foreground="#e8e800")
        self.vtubutton.configure(highlightbackground="#d9d9d9")
        self.vtubutton.configure(highlightcolor="black")
        self.vtubutton.configure(pady="0")
        self.vtubutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.vtubutton.configure(relief="groove")
        self.vtubutton.configure(text='''Change\nUsername''')

        # CHANGE PIN BUTTON
        self.changepinbutton = tk.Button(self.Settingsframe, command=lambda: self.show_frame(self.changepinframe))
        self.changepinbutton.place(relx=0.786, rely=0.628, height=40, width=87)
        self.changepinbutton.configure(activebackground="#ececec")
        self.changepinbutton.configure(activeforeground="#000000")
        self.changepinbutton.configure(background="#000000")
        self.changepinbutton.configure(font="-family {Verdana} -size 9 -weight bold")
        self.changepinbutton.configure(disabledforeground="#a3a3a3")
        self.changepinbutton.configure(foreground="#e8e800")
        self.changepinbutton.configure(highlightbackground="#d9d9d9")
        self.changepinbutton.configure(highlightcolor="black")
        self.changepinbutton.configure(pady="0")
        self.changepinbutton.configure(relief="groove")
        self.changepinbutton.configure(text='''Change Pin''')

        # # HORIZONTAL LINE
        # self.TSeparator7 = ttk.Separator(self.overviewframe)
        # self.TSeparator7.place(relx=0.021, rely=0.819, relwidth=0.957)

        # # SIGNOUT BUTTON
        # self.sign_out_button = tk.Button(self.overviewframe, command=lambda: self.show_frame(self.Frame1))
        # self.sign_out_button.place(relx=0.752, rely=0.86, height=34, width=107)
        # self.sign_out_button.configure(activebackground="#ececec")
        # self.sign_out_button.configure(activeforeground="#000000")
        # self.sign_out_button.configure(background="#ffffff")
        # self.sign_out_button.configure(cursor="arrow")
        # self.sign_out_button.configure(disabledforeground="#a3a3a3")
        # self.sign_out_button.configure(font="-family {Verdana} -size 9 -weight bold")
        # self.sign_out_button.configure(foreground="#000000")
        # self.sign_out_button.configure(highlightbackground="#d9d9d9")
        # self.sign_out_button.configure(highlightcolor="black")
        # self.sign_out_button.configure(pady="0")
        # self.sign_out_button.configure(relief="groove")
        # self.sign_out_button.configure(text='''Sign Out''')

        # ---------------------------CONTACT US PAGE-----------------------------
        self.connect = tk.Frame(top)
        self.connect.place(relx=0.017, rely=0.022, relheight=0.935, relwidth=0.975)
        self.connect.configure(relief='groove')
        self.connect.configure(borderwidth="2")
        self.connect.configure(relief="groove")
        self.connect.configure(background="#ffffff")
        self.connect.configure(highlightbackground="#d9d9d9")
        self.connect.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.connect)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=138)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img14
        # _img14 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img14)
        self.Label1.configure(text='''Label''')

        # RETURN BACK TO OVERVIEW BUTTON
        self.contactusreturn = tk.Button(self.connect, command=lambda: self.show_frame(self.overviewframe))
        self.contactusreturn.place(relx=0.786, rely=0.060, height=34, width=105)
        self.contactusreturn.configure(activebackground="#ececec")
        self.contactusreturn.configure(activeforeground="#000000")
        self.contactusreturn.configure(background="#000000")
        self.contactusreturn.configure(disabledforeground="#a3a3a3")
        self.contactusreturn.configure(font="-family {Verdana} -size 9 -weight bold")
        self.contactusreturn.configure(foreground="#e8e800")
        self.contactusreturn.configure(highlightbackground="#d9d9d9")
        self.contactusreturn.configure(highlightcolor="black")
        self.contactusreturn.configure(pady="0")
        self.contactusreturn.configure(relief="groove")
        self.contactusreturn.configure(text='''Overview''')

        # CONNECT WITH US LABELFRAME
        self.connectlabelframe = tk.LabelFrame(self.connect)
        self.connectlabelframe.place(relx=0.103, rely=0.163, relheight=0.709, relwidth=0.795)
        self.connectlabelframe.configure(relief='groove')
        self.connectlabelframe.configure(foreground="black")
        self.connectlabelframe.configure(text='''Connect With Us''')
        self.connectlabelframe.configure(background="#ffffff")
        self.connectlabelframe.configure(highlightbackground="#d9d9d9")
        self.connectlabelframe.configure(highlightcolor="black")

        # FIND LOCATION BUTTON
        self.findlocation = tk.Button(self.connectlabelframe, command=lambda: self.show_frame(self.findlocframe))
        self.findlocation.place(relx=0.19, rely=0.150, height=50, width=300, bordermode='ignore')
        self.findlocation.configure(activebackground="#ececec")
        self.findlocation.configure(activeforeground="#000000")
        self.findlocation.configure(background="#000000")
        self.findlocation.configure(disabledforeground="#a3a3a3")
        self.findlocation.configure(font="-family {Verdana} -size 10 -weight bold")
        self.findlocation.configure(foreground="#e8e800")
        self.findlocation.configure(highlightbackground="#d9d9d9")
        self.findlocation.configure(highlightcolor="black")
        self.findlocation.configure(pady="0")
        self.findlocation.configure(text='''Find a Location''')

        # GET IN TOUCH BUTTON
        self.getintouch = tk.Button(self.connectlabelframe, command=lambda: self.show_frame(self.gettouchframe))
        self.getintouch.place(relx=0.19, rely=0.450, height=50, width=300, bordermode='ignore')
        self.getintouch.configure(activebackground="#ececec")
        self.getintouch.configure(activeforeground="#000000")
        self.getintouch.configure(background="#000000")
        self.getintouch.configure(disabledforeground="#a3a3a3")
        self.getintouch.configure(font="-family {Verdana} -size 10 -weight bold")
        self.getintouch.configure(foreground="#e8e800")
        self.getintouch.configure(highlightbackground="#d9d9d9")
        self.getintouch.configure(highlightcolor="black")
        self.getintouch.configure(pady="0")
        self.getintouch.configure(text='''Get In Touch''')

        # ------------------FIND LOCATION PAGE--------------------------------
        self.findlocframe = tk.Frame(top)
        self.findlocframe.place(relx=0.017, rely=0.022, relheight=0.935, relwidth=0.975)
        self.findlocframe.configure(relief='groove')
        self.findlocframe.configure(borderwidth="2")
        self.findlocframe.configure(background="#ffffff")
        self.findlocframe.configure(highlightbackground="#d9d9d9")
        self.findlocframe.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.findlocframe)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=138)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img16
        # _img16 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img16)
        self.Label1.configure(text='''Label''')

        # CONTACT US BUTTON
        self.findlocreturn = tk.Button(self.findlocframe, command=lambda: self.show_frame(self.connect))
        self.findlocreturn.place(relx=0.786, rely=0.060, height=34, width=105)
        self.findlocreturn.configure(activebackground="#ececec")
        self.findlocreturn.configure(activeforeground="#000000")
        self.findlocreturn.configure(background="#000000")
        self.findlocreturn.configure(disabledforeground="#a3a3a3")
        self.findlocreturn.configure(font="-family {Segoe UI} -size 9")
        self.findlocreturn.configure(foreground="#e8e800")
        self.findlocreturn.configure(highlightbackground="#d9d9d9")
        self.findlocreturn.configure(highlightcolor="black")
        self.findlocreturn.configure(pady="0")
        self.findlocreturn.configure(relief="groove")
        self.findlocreturn.configure(text='''Contact Us''')

        # FIND LOCATION LABELFRAME
        self.Labelframe1 = tk.LabelFrame(self.findlocframe)
        self.Labelframe1.place(relx=0.103, rely=0.163, relheight=0.709, relwidth=0.795)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Find Location''')
        self.Labelframe1.configure(background="#ffffff")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        # LOCATION LABEL
        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(relx=0.22, rely=0.2, relheight=0.13, relwidth=0.56, bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''We have locations somewhere around and we promise you can't be stranded. Check our locations below:''')

        # LOCATION LABEL
        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(relx=0.34, rely=0.3, relheight=0.109, relwidth=0.309, bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Lagos: No 7, Alakija way, Off Lekki Bridge, Ajah, Ikeja state.''')

        # LOCATION LABEL
        self.Label6_1 = tk.Label(self.Labelframe1)
        self.Label6_1.place(relx=0.37, rely=0.4, relheight=0.109, relwidth=0.272, bordermode='ignore')
        self.Label6_1.configure(activebackground="#f9f9f9")
        self.Label6_1.configure(activeforeground="black")
        self.Label6_1.configure(background="#ffffff")
        self.Label6_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1.configure(foreground="#000000")
        self.Label6_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1.configure(highlightcolor="black")
        self.Label6_1.configure(text='''IBADAN: No 6, Eleko way, Alagbado, Ibadan state.''')

        # LOCATION LABEL
        self.Label6_2 = tk.Label(self.Labelframe1)
        self.Label6_2.place(relx=0.40, rely=0.5, relheight=0.109, relwidth=0.22, bordermode='ignore')
        self.Label6_2.configure(activebackground="#f9f9f9")
        self.Label6_2.configure(activeforeground="black")
        self.Label6_2.configure(background="#ffffff")
        self.Label6_2.configure(disabledforeground="#a3a3a3")
        self.Label6_2.configure(foreground="#000000")
        self.Label6_2.configure(highlightbackground="#d9d9d9")
        self.Label6_2.configure(highlightcolor="black")
        self.Label6_2.configure(text='''ABA: Chief Ndidi Estate, Aba, Edo state''')

        # -------------------------GET IN TOUCH PAGE----------------------
        self.gettouchframe = tk.Frame(top)
        self.gettouchframe.place(relx=0.017, rely=0.022, relheight=0.935, relwidth=0.975)
        self.gettouchframe.configure(relief='groove')
        self.gettouchframe.configure(borderwidth="2")
        self.gettouchframe.configure(relief="groove")
        self.gettouchframe.configure(background="#d9d9d9")
        self.gettouchframe.configure(highlightbackground="#d9d9d9")
        self.gettouchframe.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.gettouchframe)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=138)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img15
        # _img15 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img15)
        self.Label1.configure(text='''Label''')

        # CONTACT US PAGE
        self.getintouchreturn = tk.Button(self.gettouchframe, command=lambda: self.show_frame(self.connect))
        self.getintouchreturn.place(relx=0.786, rely=0.060, height=34, width=105)
        self.getintouchreturn.configure(activebackground="#ececec")
        self.getintouchreturn.configure(activeforeground="#000000")
        self.getintouchreturn.configure(background="#000000")
        self.getintouchreturn.configure(disabledforeground="#a3a3a3")
        self.getintouchreturn.configure(font="-family {Segoe UI} -size 9")
        self.getintouchreturn.configure(foreground="#e8e800")
        self.getintouchreturn.configure(highlightbackground="#d9d9d9")
        self.getintouchreturn.configure(highlightcolor="black")
        self.getintouchreturn.configure(pady="0")
        self.getintouchreturn.configure(relief="groove")
        self.getintouchreturn.configure(text='''Contact Us''')

        # GET IN TOUCH LABELFRAME
        self.gettouchlframe = tk.LabelFrame(self.gettouchframe)
        self.gettouchlframe.place(relx=0.103, rely=0.163, relheight=0.709, relwidth=0.795)
        self.gettouchlframe.configure(relief='groove')
        self.gettouchlframe.configure(foreground="black")
        self.gettouchlframe.configure(text='''Get in Touch''')
        self.gettouchlframe.configure(background="#ffffff")
        self.gettouchlframe.configure(highlightbackground="#d9d9d9")
        self.gettouchlframe.configure(highlightcolor="black")

        # DESCRIPTION LABEL
        self.Label3 = tk.Label(self.gettouchframe)
        self.Label3.place(relx=0.25, rely=0.3, relheight=0.13, relwidth=0.5, bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''EDHAC Bank is a small scale microfinance established by:''')

        # DESCRIPTION LABEL
        self.Label4 = tk.Label(self.gettouchframe)
        self.Label4.place(relx=0.250, rely=0.384, relheight=0.13, relwidth=0.50, bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Verdana} -size 9")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Ofoma Oluebube, Aderibigbe David, Akinyemi Hope, Adebiyi Alameen and Chike Clinton''')

        # -------------------CHANGE NAME PAGE--------------------------
        self.changename = tk.Frame(top)
        self.changename.place(relx=0.017, rely=0.022, relheight=0.935, relwidth=0.975)
        self.changename.configure(relief='groove')
        self.changename.configure(borderwidth="2")
        self.changename.configure(relief="groove")
        self.changename.configure(background="#ffffff")
        self.changename.configure(highlightbackground="#d9d9d9")
        self.changename.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.changename)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=138)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img13
        # _img13 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img13)
        self.Label1.configure(text='''Label''')

        # BACK TO OVERVIEW BUTTON
        self.vtureturn = tk.Button(self.changename, command=lambda: self.show_frame(self.overviewframe))
        self.vtureturn.place(relx=0.786, rely=0.060, height=34, width=105)
        self.vtureturn.configure(activebackground="#ececec")
        self.vtureturn.configure(activeforeground="#000000")
        self.vtureturn.configure(background="#000000")
        self.vtureturn.configure(disabledforeground="#a3a3a3")
        self.vtureturn.configure(font="-family {Segoe UI} -size 9")
        self.vtureturn.configure(foreground="#e8e800")
        self.vtureturn.configure(highlightbackground="#d9d9d9")
        self.vtureturn.configure(highlightcolor="black")
        self.vtureturn.configure(pady="0")
        self.vtureturn.configure(relief="groove")
        self.vtureturn.configure(text='''Overview''')

        # CHANGE NAME LABELFRAME
        self.changenameframe = tk.LabelFrame(self.changename)
        self.changenameframe.place(relx=0.103, rely=0.163, relheight=0.709, relwidth=0.795)
        self.changenameframe.configure(relief='groove')
        self.changenameframe.configure(foreground="black")
        self.changenameframe.configure(text='''Change Name''')
        self.changenameframe.configure(background="#ffffff")
        self.changenameframe.configure(highlightbackground="#d9d9d9")
        self.changenameframe.configure(highlightcolor="black")

        # ACCOUNT NUMBER LABEL
        self.changenameLabel = tk.Label(self.changenameframe)
        self.changenameLabel.place(x=29, y=86, height=33, width=120, bordermode='ignore')
        self.changenameLabel.configure(activebackground="#f9f9f9")
        self.changenameLabel.configure(activeforeground="black")
        self.changenameLabel.configure(background="#ffffff")
        self.changenameLabel.configure(disabledforeground="#a3a3a3")
        self.changenameLabel.configure(font="-family {Verdana} -size 9 -weight bold")
        self.changenameLabel.configure(foreground="#000000")
        self.changenameLabel.configure(highlightbackground="#d9d9d9")
        self.changenameLabel.configure(highlightcolor="black")
        self.changenameLabel.configure(text='''Account number :''')

        # ACCOUNT NUMBER ENTRY
        self.changenameEntry1 = tk.Entry(self.changenameframe)
        self.changenameEntry1.place(x=166, y=90, height=27, width=204, bordermode='ignore')
        self.changenameEntry1.configure(background="white")
        self.changenameEntry1.configure(disabledforeground="#a3a3a3")
        self.changenameEntry1.configure(font="TkFixedFont")
        self.changenameEntry1.configure(foreground="#000000")
        self.changenameEntry1.configure(highlightbackground="#d9d9d9")
        self.changenameEntry1.configure(highlightcolor="black")
        self.changenameEntry1.configure(insertbackground="black")
        self.changenameEntry1.configure(selectbackground="blue")
        self.changenameEntry1.configure(selectforeground="white")

        # AMOUNT LABEL
        self.changenameLabel2 = tk.Label(self.changenameframe)
        self.changenameLabel2.place(x=19, y=148, height=40, width=116, bordermode='ignore')
        self.changenameLabel2.configure(activebackground="#f9f9f9")
        self.changenameLabel2.configure(activeforeground="black")
        self.changenameLabel2.configure(background="#ffffff")
        self.changenameLabel2.configure(disabledforeground="#a3a3a3")
        self.changenameLabel2.configure(font="-family {Verdana} -size 9 -weight bold")
        self.changenameLabel2.configure(foreground="#000000")
        self.changenameLabel2.configure(highlightbackground="#d9d9d9")
        self.changenameLabel2.configure(highlightcolor="black")
        self.changenameLabel2.configure(text='''Amount :''')

        # AMOUNT ENTRY
        self.changenameEntry2 = tk.Entry(self.changenameframe)
        self.changenameEntry2.place(x=166, y=159, height=27, width=204, bordermode='ignore')
        self.changenameEntry2.configure(background="white")
        self.changenameEntry2.configure(disabledforeground="#a3a3a3")
        self.changenameEntry2.configure(font="TkFixedFont")
        self.changenameEntry2.configure(foreground="#000000")
        self.changenameEntry2.configure(highlightbackground="#d9d9d9")
        self.changenameEntry2.configure(highlightcolor="black")
        self.changenameEntry2.configure(insertbackground="black")
        self.changenameEntry2.configure(selectbackground="blue")
        self.changenameEntry2.configure(selectforeground="white")

        # CHANGE (SUBMIT) BUTTON
        self.changenameButton1 = tk.Button(self.changenameframe, command=lambda: self.depositing_thread(None))
        self.changenameButton1.place(x=156, y=240, height=34, width=150, bordermode='ignore')
        self.changenameButton1.configure(activebackground="#ececec")
        self.changenameButton1.configure(activeforeground="#000000")
        self.changenameButton1.configure(background="#000000")
        self.changenameButton1.configure(cursor="arrow")
        self.changenameButton1.configure(disabledforeground="#a3a3a3")
        self.changenameButton1.configure(font="-family {Verdana} -size 10 -weight bold")
        self.changenameButton1.configure(foreground="#e8e800")
        self.changenameButton1.configure(highlightbackground="#d9d9d9")
        self.changenameButton1.configure(highlightcolor="black")
        self.changenameButton1.configure(pady="0")
        self.changenameButton1.configure(text='''Change''')

        # -------------------CHANGE PIN PAGE-----------------------------------
        self.changepinframe = tk.Frame(top)
        self.changepinframe.place(relx=0.017, rely=0.022, relheight=0.935, relwidth=0.975)
        self.changepinframe.configure(relief='groove')
        self.changepinframe.configure(borderwidth="2")
        self.changepinframe.configure(relief="groove")
        self.changepinframe.configure(background="#ffffff")
        self.changepinframe.configure(highlightbackground="#d9d9d9")
        self.changepinframe.configure(highlightcolor="black")

        # LOGO
        self.Label1 = tk.Label(self.changepinframe)
        self.Label1.place(relx=0.042, rely=0.015, height=98, width=138)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img10
        # _img10 = ImageTk.PhotoImage(file=photo_location)
        # self.Label1.configure(image=_img10)
        self.Label1.configure(text='''Label''')

        # RETURN TO OVERVIEW PAGE
        self.sreturn_overview = tk.Button(self.changepinframe, command=lambda: self.show_frame(self.overviewframe))
        self.sreturn_overview.place(relx=0.786, rely=0.060, height=34, width=105)
        self.sreturn_overview.configure(activebackground="#ececec")
        self.sreturn_overview.configure(activeforeground="#000000")
        self.sreturn_overview.configure(background="#000000")
        self.sreturn_overview.configure(disabledforeground="#a3a3a3")
        self.sreturn_overview.configure(font="-family {Segoe UI} -size 9")
        self.sreturn_overview.configure(foreground="#e8e800")
        self.sreturn_overview.configure(highlightbackground="#d9d9d9")
        self.sreturn_overview.configure(highlightcolor="black")
        self.sreturn_overview.configure(pady="0")
        self.sreturn_overview.configure(relief="groove")
        self.sreturn_overview.configure(text='''Overview''')

        # CHANGE PIN LABELFRAME
        self.changeLabelframe2 = tk.LabelFrame(self.changepinframe)
        self.changeLabelframe2.place(x=39, y=145, height=453, width=522)
        self.changeLabelframe2.configure(relief='groove')
        self.changeLabelframe2.configure(foreground="black")
        self.changeLabelframe2.configure(text='''Change Pin''')
        self.changeLabelframe2.configure(background="#ffffff")
        self.changeLabelframe2.configure(highlightbackground="#d9d9d9")
        self.changeLabelframe2.configure(highlightcolor="black")

        # OLD PIN LABEL
        self.changeLabel2 = tk.Label(self.changeLabelframe2)
        self.changeLabel2.place(x=29, y=86, height=33, width=108, bordermode='ignore')
        self.changeLabel2.configure(activebackground="#f9f9f9")
        self.changeLabel2.configure(activeforeground="black")
        self.changeLabel2.configure(background="#ffffff")
        self.changeLabel2.configure(disabledforeground="#a3a3a3")
        self.changeLabel2.configure(font="-family {Verdana} -size 10 -weight bold")
        self.changeLabel2.configure(foreground="#000000")
        self.changeLabel2.configure(highlightbackground="#d9d9d9")
        self.changeLabel2.configure(highlightcolor="black")
        self.changeLabel2.configure(text='''Old pin :''')

        # OLD PIN ENTRY
        self.changeEntry1 = tk.Entry(self.changeLabelframe2)
        self.changeEntry1.place(x=166, y=90, height=27, width=204, bordermode='ignore')
        self.changeEntry1.configure(background="white")
        self.changeEntry1.configure(disabledforeground="#a3a3a3")
        self.changeEntry1.configure(font="TkFixedFont")
        self.changeEntry1.configure(foreground="#000000")
        self.changeEntry1.configure(highlightbackground="#d9d9d9")
        self.changeEntry1.configure(highlightcolor="black")
        self.changeEntry1.configure(insertbackground="black")
        self.changeEntry1.configure(selectbackground="blue")
        self.changeEntry1.configure(selectforeground="white")

        # NEW PIN LABEL
        self.changeLabel3 = tk.Label(self.changeLabelframe2)
        self.changeLabel3.place(x=19, y=148, height=40, width=116, bordermode='ignore')
        self.changeLabel3.configure(activebackground="#f9f9f9")
        self.changeLabel3.configure(activeforeground="black")
        self.changeLabel3.configure(background="#ffffff")
        self.changeLabel3.configure(disabledforeground="#a3a3a3")
        self.changeLabel3.configure(font="-family {Verdana} -size 10 -weight bold")
        self.changeLabel3.configure(foreground="#000000")
        self.changeLabel3.configure(highlightbackground="#d9d9d9")
        self.changeLabel3.configure(highlightcolor="black")
        self.changeLabel3.configure(text='''New pin :''')

        # NEW PIN ENTRY
        self.changeEntry2 = tk.Entry(self.changeLabelframe2)
        self.changeEntry2.place(x=166, y=159, height=27, width=204, bordermode='ignore')
        self.changeEntry2.configure(background="white")
        self.changeEntry2.configure(disabledforeground="#a3a3a3")
        self.changeEntry2.configure(font="TkFixedFont")
        self.changeEntry2.configure(foreground="#000000")
        self.changeEntry2.configure(highlightbackground="#d9d9d9")
        self.changeEntry2.configure(highlightcolor="black")
        self.changeEntry2.configure(insertbackground="black")
        self.changeEntry2.configure(selectbackground="blue")
        self.changeEntry2.configure(selectforeground="white")

        # CHANGE (SUBMIT) BUTTON
        self.changeButton1 = tk.Button(self.changeLabelframe2, command=lambda: self.reset_thread(None))
        self.changeButton1.place(x=156, y=240, height=34, width=150, bordermode='ignore')
        self.changeButton1.configure(activebackground="#ececec")
        self.changeButton1.configure(activeforeground="#000000")
        self.changeButton1.configure(background="#000000")
        self.changeButton1.configure(cursor="arrow")
        self.changeButton1.configure(disabledforeground="#a3a3a3")
        self.changeButton1.configure(font="-family {Verdana} -size 10 -weight bold")
        self.changeButton1.configure(foreground="#e8e800")
        self.changeButton1.configure(highlightbackground="#d9d9d9")
        self.changeButton1.configure(highlightcolor="black")
        self.changeButton1.configure(pady="0")
        self.changeButton1.configure(text='''Change''')    

        # ---------------------------ADMIN PAGE--------------------------------
        self.adminframe = tk.Frame(top)
        self.adminframe.place(x=0, y=0, height=655, width=575)
        self.adminframe.configure(relief='groove')
        self.adminframe.configure(borderwidth="2")
        self.adminframe.configure(relief="groove")
        self.adminframe.configure(background="#ffffff")

        # LOGO
        self.Adminlabel1 = tk.Label(self.adminframe)
        self.Adminlabel1.place(x=10, y=10, height=112, width=144)
        self.Adminlabel1.configure(background="#ffffff")
        self.Adminlabel1.configure(disabledforeground="#a3a3a3")
        self.Adminlabel1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img20
        # _img20 = ImageTk.PhotoImage(file=photo_location)
        # self.Adminlabel1.configure(image=_img20)
        self.Adminlabel1.configure(text='''Label''')

        # LOGOUT BUTTON
        self.adButton1_4 = tk.Button(self.adminframe, command=lambda: self.show_frame(self.Frame1))
        self.adButton1_4.place(x=420, y=30, height=34, width=117)
        self.adButton1_4.configure(activebackground="#ececec")
        self.adButton1_4.configure(activeforeground="#000000")
        self.adButton1_4.configure(background="#000000")
        self.adButton1_4.configure(disabledforeground="#a3a3a3")
        self.adButton1_4.configure(font="-family {Verdana} -size 9 -weight bold")
        self.adButton1_4.configure(foreground="#e8e800")
        self.adButton1_4.configure(highlightbackground="#ffffff")
        self.adButton1_4.configure(highlightcolor="black")
        self.adButton1_4.configure(pady="0")
        self.adButton1_4.configure(text='''Log out''')

        # ADMIN LABELFRAME
        self.Adminlabelframe1 = tk.LabelFrame(self.adminframe)
        self.Adminlabelframe1.place(x=20, y=150, height=485, width=540)
        self.Adminlabelframe1.configure(relief='groove')
        self.Adminlabelframe1.configure(font="-family {Verdana} -size 9 -weight bold -slant italic")
        self.Adminlabelframe1.configure(foreground="black")
        self.Adminlabelframe1.configure(text='''Welcome Admin''')
        self.Adminlabelframe1.configure(background="#ffffff")

        # BANK NAME LABEL
        self.ADmessage = tk.Message(self.Adminlabelframe1)
        self.ADmessage.place(x=140, y=40, height=43, width=260, bordermode='ignore')
        self.ADmessage.configure(background="#e8e800")
        self.ADmessage.configure(font="-family {Times New Roman} -size 13 -weight bold -slant italic")
        self.ADmessage.configure(foreground="#000000")
        self.ADmessage.configure(highlightbackground="#d9d9d9")
        self.ADmessage.configure(highlightcolor="black")
        self.ADmessage.configure(text='''EDHAC BANK''')
        self.ADmessage.configure(width=260)

        # CHECK USER BUTTON
        self.accdetails = tk.Button(self.Adminlabelframe1, command=lambda: self.show_frame(self.checkacc))
        self.accdetails.place(x=70, y=160, height=44, width=367, bordermode='ignore')
        self.accdetails.configure(activebackground="#ececec")
        self.accdetails.configure(activeforeground="#000000")
        self.accdetails.configure(background="#000000")
        self.accdetails.configure(disabledforeground="#a3a3a3")
        self.accdetails.configure(font="-family {Verdana} -size 9 -weight bold")
        self.accdetails.configure(foreground="#e8e800")
        self.accdetails.configure(highlightbackground="#ffffff")
        self.accdetails.configure(highlightcolor="black")
        self.accdetails.configure(pady="0")
        self.accdetails.configure(text='''Check users account details''')

        # MAKE DEPOSIT BUTTON
        self.payment = tk.Button(self.Adminlabelframe1, command=lambda: self.show_frame(self.deposit))
        self.payment.place(x=70, y=260, height=44, width=367, bordermode='ignore')
        self.payment.configure(activeforeground="#000000")
        self.payment.configure(activebackground="#ececec")
        self.payment.configure(background="#000000")
        self.payment.configure(disabledforeground="#a3a3a3")
        self.payment.configure(font="-family {Verdana} -size 9 -weight bold")
        self.payment.configure(foreground="#e8e800")
        self.payment.configure(highlightbackground="#ffffff")
        self.payment.configure(highlightcolor="black")
        self.payment.configure(pady="0")
        self.payment.configure(text='''Make deposit''')

        # DELETE ACCOUNT BUTTON
        self.Delacc = tk.Button(self.Adminlabelframe1, command=lambda: self.show_frame(self.del_frame))
        self.Delacc.place(x=70, y=360, height=44, width=367, bordermode='ignore')
        self.Delacc.configure(activebackground="#ececec")
        self.Delacc.configure(activeforeground="#000000")
        self.Delacc.configure(background="#000000")
        self.Delacc.configure(disabledforeground="#a3a3a3")
        self.Delacc.configure(font="-family {Verdana} -size 9 -weight bold")
        self.Delacc.configure(foreground="#e8e800")
        self.Delacc.configure(highlightbackground="#ffffff")
        self.Delacc.configure(highlightcolor="black")
        self.Delacc.configure(pady="0")
        self.Delacc.configure(text='''Delete an account''')

        # ----------------CHECK ACCOUNT DETIALS---------------------------
        self.checkacc = tk.Frame(top)
        self.checkacc.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.checkacc.configure(relief='groove')
        self.checkacc.configure(borderwidth="2")
        self.checkacc.configure(background="#ffffff")

        # CHECK ACCOUNT DETAILS LABELFRAME
        self.checkaccLabelframe = tk.LabelFrame(self.checkacc)
        self.checkaccLabelframe.place(x=39, y=145, height=453, width=522)
        self.checkaccLabelframe.configure(relief='groove')
        self.checkaccLabelframe.configure(font="-family {Arial} -size 10 -weight bold")
        self.checkaccLabelframe.configure(foreground="black")
        self.checkaccLabelframe.configure(text='''Check Account Details''')
        self.checkaccLabelframe.configure(background="#ffffff")

        # ACCOUNT NUMBER LABEL
        self.checkaccLabel1 = tk.Label(self.checkaccLabelframe)
        self.checkaccLabel1.place(relx=0.073, rely=0.269, height=31, width=154, bordermode='ignore')
        self.checkaccLabel1.configure(background="#ffffff")
        self.checkaccLabel1.configure(disabledforeground="#a3a3a3")
        self.checkaccLabel1.configure(font="-family {Verdana} -size 10 -weight bold")
        self.checkaccLabel1.configure(foreground="#000000")
        self.checkaccLabel1.configure(text='''Account number :''')

        # ACCOUNT NUMBER ENTRY
        self.checkaccEntry1 = tk.Entry(self.checkaccLabelframe)
        self.checkaccEntry1.place(relx=0.382, rely=0.269, height=30, relwidth=0.335, bordermode='ignore')
        self.checkaccEntry1.configure(background="white")
        self.checkaccEntry1.configure(disabledforeground="#a3a3a3")
        self.checkaccEntry1.configure(font="TkFixedFont")
        self.checkaccEntry1.configure(foreground="#000000")
        self.checkaccEntry1.configure(insertbackground="black")

        # CONTINUE (SUBMIT) BUTTON
        self.checkaccb2 = tk.Button(self.checkaccLabelframe, command= self.display_details)
        self.checkaccb2.place(relx=0.382, rely=0.478, height=30, width=107, bordermode='ignore')
        self.checkaccb2.configure(activebackground="#ececec")
        self.checkaccb2.configure(activeforeground="#000000")
        self.checkaccb2.configure(background="#000000")
        self.checkaccb2.configure(borderwidth="1")
        self.checkaccb2.configure(disabledforeground="#a3a3a3")
        self.checkaccb2.configure(font="-family {Verdana} -size 9 -weight bold")
        self.checkaccb2.configure(foreground="#e8e800")
        self.checkaccb2.configure(highlightbackground="#d9d9d9")
        self.checkaccb2.configure(highlightcolor="black")
        self.checkaccb2.configure(pady="0")
        self.checkaccb2.configure(text='''Continue''')

        # HOME BUTTON
        self.checkButton1_4 = tk.Button(self.checkacc, command=lambda: self.show_frame(self.adminframe))
        self.checkButton1_4.place(x=420, y=30, height=34, width=117)
        self.checkButton1_4.configure(activebackground="#ececec")
        self.checkButton1_4.configure(activeforeground="#000000")
        self.checkButton1_4.configure(background="#000000")
        self.checkButton1_4.configure(disabledforeground="#a3a3a3")
        self.checkButton1_4.configure(font="-family {Verdana} -size 9 -weight bold")
        self.checkButton1_4.configure(foreground="#e8e800")
        self.checkButton1_4.configure(highlightbackground="#ffffff")
        self.checkButton1_4.configure(highlightcolor="black")
        self.checkButton1_4.configure(pady="0")
        self.checkButton1_4.configure(text='''Home''')

        self.checkacc2 = tk.Frame(top)
        self.checkacc2.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.006)
        self.checkacc2.configure(relief='groove')
        self.checkacc2.configure(borderwidth="2")
        self.checkacc2.configure(relief="groove")
        self.checkacc2.configure(background="#ffffff")

        self.checkListbox1 = tk.Listbox(self.checkacc2)
        self.checkListbox1.place(relx=0.05, rely=0.066, relheight=0.84, relwidth=0.883)
        self.checkListbox1.configure(background="white")
        self.checkListbox1.configure(disabledforeground="#a3a3a3")
        self.checkListbox1.configure(font="TkFixedFont")
        self.checkListbox1.configure(foreground="#000000")

        self.checkaccb1 = tk.Button(self.checkacc2)
        self.checkaccb1.place(relx=0.711, rely=0.044, height=30, width=97)
        self.checkaccb1.configure(activebackground="#ececec")
        self.checkaccb1.configure(activeforeground="#000000")
        self.checkaccb1.configure(background="#000000")
        self.checkaccb1.configure(disabledforeground="#a3a3a3")
        self.checkaccb1.configure(font="-family {Verdana} -size 9 -weight bold")
        self.checkaccb1.configure(foreground="#e8e800")
        self.checkaccb1.configure(highlightbackground="#d9d9d9")
        self.checkaccb1.configure(highlightcolor="black")
        self.checkaccb1.configure(pady="0")
        self.checkaccb1.configure(text='''Home''')

        # ----------------DEPOSIT FRAME-----------------------
        self.deposit = tk.Frame(top)
        self.deposit.place(x=8, y=10, height=745, width=590)
        self.deposit.configure(relief='groove')
        self.deposit.configure(borderwidth="2")
        self.deposit.configure(relief="groove")
        self.deposit.configure(background="#ffffff")
        self.deposit.configure(highlightbackground="#d9d9d9")
        self.deposit.configure(highlightcolor="black")

        # LOGO
        self.depLabel23 = tk.Label(self.deposit)
        self.depLabel23.place(x=19, y=10, height=103, width=151)
        self.depLabel23.configure(background="#d9d9d9")
        self.depLabel23.configure(disabledforeground="#a3a3a3")
        self.depLabel23.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img21
        # _img21 = ImageTk.PhotoImage(file=photo_location)
        # self.depLabel23.configure(image=_img21)
        self.depLabel23.configure(text='''Label''')

        # DEPOSIT LABELFRAME
        self.Deplabelframe = tk.LabelFrame(self.deposit)
        self.Deplabelframe.place(x=39, y=145, height=453, width=522)
        self.Deplabelframe.configure(relief='groove')
        self.Deplabelframe.configure(foreground="black")
        self.Deplabelframe.configure(text='''LOGIN''')
        self.Deplabelframe.configure(background="#ffffff")
        self.Deplabelframe.configure(highlightbackground="#d9d9d9")
        self.Deplabelframe.configure(highlightcolor="black")

        # ACCOUNT NUMBER LABEL
        self.depLabel = tk.Label(self.Deplabelframe)
        self.depLabel.place(x=29, y=86, height=33, width=120, bordermode='ignore')
        self.depLabel.configure(activebackground="#f9f9f9")
        self.depLabel.configure(activeforeground="black")
        self.depLabel.configure(background="#ffffff")
        self.depLabel.configure(disabledforeground="#a3a3a3")
        self.depLabel.configure(font="-family {Verdana} -size 9 -weight bold")
        self.depLabel.configure(foreground="#000000")
        self.depLabel.configure(highlightbackground="#d9d9d9")
        self.depLabel.configure(highlightcolor="black")
        self.depLabel.configure(text='''Account number :''')

        # ACCOUNT NUMBER ENTRY
        self.depEntry1 = tk.Entry(self.Deplabelframe)
        self.depEntry1.place(x=166, y=90, height=27, width=204, bordermode='ignore')
        self.depEntry1.configure(background="white")
        self.depEntry1.configure(disabledforeground="#a3a3a3")
        self.depEntry1.configure(font="TkFixedFont")
        self.depEntry1.configure(foreground="#000000")
        self.depEntry1.configure(highlightbackground="#d9d9d9")
        self.depEntry1.configure(highlightcolor="black")
        self.depEntry1.configure(insertbackground="black")
        self.depEntry1.configure(selectbackground="blue")
        self.depEntry1.configure(selectforeground="white")

        # AMOUNT LABEL
        self.depLabel2 = tk.Label(self.Deplabelframe)
        self.depLabel2.place(x=19, y=148, height=40, width=116, bordermode='ignore')
        self.depLabel2.configure(activebackground="#f9f9f9")
        self.depLabel2.configure(activeforeground="black")
        self.depLabel2.configure(background="#ffffff")
        self.depLabel2.configure(disabledforeground="#a3a3a3")
        self.depLabel2.configure(font="-family {Verdana} -size 9 -weight bold")
        self.depLabel2.configure(foreground="#000000")
        self.depLabel2.configure(highlightbackground="#d9d9d9")
        self.depLabel2.configure(highlightcolor="black")
        self.depLabel2.configure(text='''Amount :''')

        # AMOUNT ENTRY
        self.depEntry2 = tk.Entry(self.Deplabelframe)
        self.depEntry2.place(x=166, y=159, height=27, width=204, bordermode='ignore')
        self.depEntry2.configure(background="white")
        self.depEntry2.configure(disabledforeground="#a3a3a3")
        self.depEntry2.configure(font="TkFixedFont")
        self.depEntry2.configure(foreground="#000000")
        self.depEntry2.configure(highlightbackground="#d9d9d9")
        self.depEntry2.configure(highlightcolor="black")
        self.depEntry2.configure(insertbackground="black")
        self.depEntry2.configure(selectbackground="blue")
        self.depEntry2.configure(selectforeground="white")

        # SUBMIT (DEPOSIT) BUTTON
        self.depButton1 = tk.Button(self.Deplabelframe, command=lambda: self.depositing_thread(None))
        self.depButton1.place(x=156, y=240, height=34, width=150, bordermode='ignore')
        self.depButton1.configure(activebackground="#ececec")
        self.depButton1.configure(activeforeground="#000000")
        self.depButton1.configure(background="#000000")
        self.depButton1.configure(cursor="arrow")
        self.depButton1.configure(disabledforeground="#a3a3a3")
        self.depButton1.configure(font="-family {Verdana} -size 10 -weight bold")
        self.depButton1.configure(foreground="#e8e800")
        self.depButton1.configure(highlightbackground="#d9d9d9")
        self.depButton1.configure(highlightcolor="black")
        self.depButton1.configure(pady="0")
        self.depButton1.configure(text='''Submit''')

        # ------------DELETE FRAME-----------------
        self.del_frame = tk.Frame(top)
        self.del_frame.place(x=0, y=0, height=655, width=575)
        self.del_frame.configure(relief='groove')
        self.del_frame.configure(borderwidth="2")
        self.del_frame.configure(background="#ffffff")

        # LOGO
        self.del_label1 = tk.Label(self.del_frame)
        self.del_label1.place(x=10, y=10, height=112, width=144)
        self.del_label1.configure(background="#ffffff")
        self.del_label1.configure(disabledforeground="#a3a3a3")
        self.del_label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "edhac1.jpg")
        global _img23
        # _img23 = ImageTk.PhotoImage(file=photo_location)
        # self.del_label1.configure(image=_img23)
        self.del_label1.configure(text='''Label''')

        # HOME BUTTON
        self.delButton1_4 = tk.Button(self.del_frame, command=lambda: self.show_frame(self.adminframe))
        self.delButton1_4.place(x=420, y=30, height=34, width=117)
        self.delButton1_4.configure(activebackground="#ececec")
        self.delButton1_4.configure(activeforeground="#000000")
        self.delButton1_4.configure(background="#000000")
        self.delButton1_4.configure(disabledforeground="#a3a3a3")
        self.delButton1_4.configure(font="-family {Verdana} -size 9 -weight bold")
        self.delButton1_4.configure(foreground="#e8e800")
        self.delButton1_4.configure(highlightbackground="#ffffff")
        self.delButton1_4.configure(highlightcolor="black")
        self.delButton1_4.configure(pady="0")
        self.delButton1_4.configure(text='''Home''')

        # DELETE ACCOUNT LABELFRAME
        self.del_labelframe1 = tk.LabelFrame(self.del_frame)
        self.del_labelframe1.place(x=20, y=150, height=485, width=540)
        self.del_labelframe1.configure(relief='groove')
        self.del_labelframe1.configure(font="-family {Verdana} -size 9 -weight bold -slant italic")
        self.del_labelframe1.configure(foreground="black")
        self.del_labelframe1.configure(text='''Delete an account''')
        self.del_labelframe1.configure(background="#ffffff")

        # ACCOUNT NUMBER LABEL
        self.delacc = tk.Label(self.del_labelframe1)
        self.delacc.place(x=19, y=148, height=40, width=140, bordermode='ignore')
        self.delacc.configure(activebackground="#f9f9f9")
        self.delacc.configure(activeforeground="black")
        self.delacc.configure(background="#ffffff")
        self.delacc.configure(disabledforeground="#a3a3a3")
        self.delacc.configure(font="-family {Verdana} -size 10 -weight bold")
        self.delacc.configure(foreground="#000000")
        self.delacc.configure(highlightbackground="#d9d9d9")
        self.delacc.configure(highlightcolor="black")
        self.delacc.configure(text='''Account number :''')

        # ACCOUNT NUMBER ENTRY
        self.delentry = tk.Entry(self.del_labelframe1)
        self.delentry.place(x=180, y=159, height=27, width=204, bordermode='ignore')
        self.delentry.configure(background="white")
        self.delentry.configure(disabledforeground="#a3a3a3")
        self.delentry.configure(font="TkFixedFont")
        self.delentry.configure(foreground="#000000")
        self.delentry.configure(highlightbackground="#d9d9d9")
        self.delentry.configure(highlightcolor="black")
        self.delentry.configure(insertbackground="black")
        self.delentry.configure(selectbackground="blue")
        self.delentry.configure(selectforeground="white")

        # DELETE BUTTON
        self.delaccButton1 = tk.Button(self.del_labelframe1, command=lambda: self.del_account())
        self.delaccButton1.place(x=156, y=240, height=30, width=140, bordermode='ignore')
        self.delaccButton1.configure(activebackground="#ececec")
        self.delaccButton1.configure(activeforeground="#000000")
        self.delaccButton1.configure(background="#000000")
        self.delaccButton1.configure(cursor="arrow")
        self.delaccButton1.configure(disabledforeground="#a3a3a3")
        self.delaccButton1.configure(font="-family {Verdana} -size 10 -weight bold")
        self.delaccButton1.configure(foreground="#e8e800")
        self.delaccButton1.configure(highlightbackground="#d9d9d9")
        self.delaccButton1.configure(highlightcolor="black")
        self.delaccButton1.configure(pady="0")
        self.delaccButton1.configure(text='''Delete''')

        self.show_frame(self.Frame1)

        # ------------------------RAISE A FRAME METHOD-----------------------------

    def show_frame(self, context):
        self.context = context
        self.context.tkraise()

    # def combine_funcs(self):
    #     def combined_func(*args, **kwargs):
    #         for f in funcs:
    #             f(*args, **kwargs)
    #     return combined_func()

    def validate_acc(self):
        time.sleep(0.2)
        submitOK = True
        name = self.Entry3.get()
        email = self.Entry4.get()
        dob = self.Entry5.get()
        phone = self.Entry6.get()
        address = self.Entry7.get()

        # ------------Validate Name Pattern-------------------
        name_pattern = '\\w{4,}\\S'
        name_result = re.match(name_pattern, name)

        if not name_result:
            submitOK = False
            messagebox.showerror("Error", "Invalid name!")
        # "^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[-/.](19|20)\\d\\d$"

        #------------Validate Email pattern-------------------
        email_pattern = '\\w+@{1}\\w+\\S'
        email_result = re.match(email_pattern, email)

        if not email_result:
            submitOK = False
            messagebox.showerror("Error", "Invalid email!")

        # ------------Validate DOB Pattern-------------------
        dob_pattern = '^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[-/.](19|20)\\d\\d$'
        dob_result = re.match(dob_pattern, dob)

        if not dob_result:
            submitOK = False
            messagebox.showerror("Error", "Invalid date of birth!")

        # ------------Validate Phone Number Pattern-------------------
        phone_pattern = '\\d{11}'
        phone_result = re.match(phone_pattern, phone)

        if not phone_result:
            submitOK = False
            messagebox.showerror("Error", "Invalid phone number!")

        if submitOK == False:
            return False
        else:
            messagebox.showinfo("Success", "Account created Successfully.")
            Acc_num = random.randint(1111111111, 9999999999)

            message = [Acc_num, name, email, dob, phone, address, "account"]  # "yes", "register"

            self.s.send(str.encode(json.dumps(message)))
            data = self.s.recv(1024)
            message_json = bytes.decode(data)
            result = json.loads(message_json)
            print(result)

            self.show_frame(self.Registration)

        # if self.rad1.get():
        #     self.cursor.execute("INSERT INTO reg_bank(gender) VALUES('male')")
        #     self.conn.commit

    def validate(self):
        time.sleep(0.2)
        # global account
        # global username
        # global password
        submitOK = True
        # email = self.email.get()
        account = self.Entry8.get()
        username = self.Entry9.get()
        pin = self.Entry10.get()
        c_pin = self.Entry10_1.get()

        username_pattern = '\\w{4,}\\S'
        username_result = re.match(username_pattern, username)

        if not username_result:
            submitOK = False
            messagebox.showerror("Error", "Invalid username!")

        pin_pattern = '[\\d{4}]'
        pin_result = re.match(pin_pattern, pin)

        if not pin_result:
            submitOK = False
            messagebox.showerror("Error",
                                 "Password must contain at least 4 numbers!")
        # elif len(password) < 8:
        #     submitOK = False
        #     messagebox.showerror("Error", "Password must contain at least 8 characters!")
        elif pin != c_pin:
            submitOK = False
            messagebox.showerror("Error", "Password Mismatch!")

        if submitOK == False:
            return False
        else:
            user_id = random.randint(99999, 9999999)

            message = [user_id, account, username, pin, "register"]  # "yes", "register"
            print("message is")
            print(message)
            self.s.send(str.encode(json.dumps(message)))
            data = self.s.recv(1024)
            message_json = bytes.decode(data)
            result = json.loads(message_json)
            print(result)

            messagebox.showinfo("Success", "User Registered Successfully.")

            self.show_frame(self.login)

        # def account_val(self):
        #     submitOK = true
        #         user= self.Entry3.get()
        #
        #
        #
        #     if submitOK == False:
        #         return False
        #     else:
        #         messagebox.showinfo("Success", "User Registered Successfully.")
        #         user_id = random.randint(99999, 9999999)
        #
        #         data = self.s.recv(1024)
        #         # print(bytes.decode(data))
        #         message = [uid, user, name, email, phone, address, gender, marry, acc, "account"]
        #
        #
        #         self.s.send(str.encode(json.dumps(message)))
        #         data = self.s.recv(1024)
        #         message_json = bytes.decode(data)
        #         result = json.loads(message_json)
        #         print(result)
        #         self.s.close()
        #
        #         self.show_frame(self.login)
        #

    def authenticate(self):
        time.sleep(0.2)
        username = self.Entry1.get()
        pin = self.Entry2.get()
        my_shelve = shelve.open("usershelf", flag="n")
        my_shelve['username'] = username

        message = [username, pin, "login"]
        self.s.send(str.encode(json.dumps(message)))
        resp = self.s.recv(1024)
        result = json.loads(bytes.decode(resp))

        # self.cursor.execute(
        #     "SELECT * FROM tbl_users WHERE username = '{}' AND password = '{}'".format(username,
        #                                                                                password))
        # result = self.cursor.fetchall()

        print(result)

        if not result:
            messagebox.showerror("Error", "Invalid username or pin.")
        else:
            if "admin" in result[0]:
                self.show_frame(self.adminframe)
            else:
                self.show_name()
                self.show_acc_num()
                self.show_frame(self.overviewframe)

    # def logout(self):
    #     time.sleep(0.2)
    #     message = ["logout"]
    #     self.s.send(str.encode(message))
    def display_details(self):
        acc_num = self.checkaccEntry1.get()
        self.cursor.execute("SELECT * FROM reg_bank WHERE Acc_num ='{}'".format(acc_num))
        result = self.cursor.fetchall()
        displist = []
        for i in result[0]:
            displist.append(i)
        for j in displist:
            self.checkListbox1.insert(tk.END, j)

        self.conn.commit()
        self.show_frame(self.checkacc2)

    def show_balance(self):
        time.sleep(0.2)
        my_shelve = shelve.open("usershelf")
        test = my_shelve.get("username")
        self.cursor.execute("SELECT account_number FROM reg_app WHERE username = '{}'".format(test))
        result = self.cursor.fetchall()
        print("result is")
        print(result[0])
        acc_num = str(result[0])
        acc_num = acc_num.strip("\',()")
        print("acc_num is ")
        print(acc_num)
        self.cursor.execute("SELECT balance FROM amount WHERE account_number = '{}'".format(acc_num))
        results = self.cursor.fetchall()
        print("results is")
        print(results[0])
        bal = str(results[0])
        bal = bal.strip("\',()")
        print("bal is")
        print(bal)
        self.balance.configure(text='''N{}'''.format(bal))

        self.conn.commit()

    def show_acc_num(self):
        time.sleep(0.2)
        username = self.Entry1.get()
        if username == "admin":
            pass
        else:
            self.cursor.execute("SELECT account_number FROM reg_app WHERE username = '{}'".format(username))
            result = self.cursor.fetchone()
            acc_num = str(result[0])
            acc_num = acc_num.strip("\',()")
            print(acc_num)
            self.active.configure(text=acc_num)

            self.conn.commit()

    def show_name(self):
        time.sleep(0.2)
        username = self.Entry1.get()
        if username != "admin":
            self.cursor.execute("SELECT account_number FROM reg_app WHERE username = '{}'".format(username))
            result = self.cursor.fetchone()
            acc_num = str(result[0])
            acc_num = acc_num.strip("\',()")
            acc_num = int(acc_num)
            print(acc_num)
            self.cursor.execute("SELECT name FROM reg_bank WHERE Acc_num = '{}'".format(acc_num))
            results = self.cursor.fetchone()
            name = str(results[0])
            name = name.strip("\',()")
            print(name)
            name = name.title()
            self.name.configure(text=name)
            self.conn.commit()

    def changepin(self):
        time.sleep(0.2)
        # acc_num = self.changeEntry3.`get()
        old_pin = self.changeEntry1.get()
        new_pin = self.changeEntry2.get()

        self.cursor.execute("UPDATE reg_app SET pin ={} WHERE pin ={}".format(new_pin, old_pin))
        messagebox.showinfo("Success", "Pin changed Successfully.")

    def changename(self):
        time.sleep(0.2)
        old_name = self.changenameEntry1.get()
        new_name = self.changenameEntry2.get()

        self.cursor.execute("UPDATE reg_app SET username ={}".format(new_name))
        messagebox.showinfo("Success", "Username changed Successfully.")

    def deeposit(self):
        time.sleep(0.2)
        amount = int(self.depEntry2.get())
        account_number = self.depEntry1.get()

        self.cursor.execute(
            "INSERT INTO amount (account_number, balance) values ('{}','{}')".format(account_number, amount))
        self.cursor.execute("SELECT balance FROM amount WHERE account_number = '{}'".format(account_number))
        result = self.cursor.fetchone()
        # result[0] += amount
        # self.cursor.execute("UPDATE amount SET balance WHERE account_number = '{}'".format(account_number))
        print("Sending deposit response...")
        if not result:
            messagebox.showerror("Error", "Account number not correct!")
        else:
            messagebox.showinfo("Success", "Deposit successful.")
        self.conn.commit()

    def transfers(self):
        time.sleep(0.2)
        account_number = self.desacct_entry.get()
        amount = int(self.ammount_entry.get())
        trans_details = self.trans_descp_entry.get()
        my_shelve = shelve.open("usershelf")
        test = my_shelve.get("username")
        self.cursor.execute(
            "INSERT INTO payment (account_number, amount, trans_details) values ('{}','{}','{}')".format(account_number,
                                                                                                         amount,
                                                                                                         trans_details))
        self.cursor.execute("SELECT account_number FROM reg_app WHERE username = '{}'".format(test))
        result = self.cursor.fetchall()
        result = str(result[0])
        result = result.strip("\',()")
        self.cursor.execute("SELECT balance FROM amount WHERE account_number = '{}'".format(result))
        bal = self.cursor.fetchall()
        bal = str(bal[0])
        bal = int(bal.strip("\',()"))
        bal -= amount
        self.cursor.execute(
            "UPDATE amount SET balance ='{}' WHERE account_number = '{}'".format(bal, result))

        self.cursor.execute("SELECT Acc_num FROM reg_bank WHERE Acc_num = '{}' ".format(account_number))
        result1 = self.cursor.fetchall()
        result1 = str(result1[0])
        result1 = result1.strip("\',()")
        print(result1)
        if account_number in result1:
            self.cursor.execute("SELECT balance FROM amount WHERE account_number = '{}'".format(account_number))
            bal1 = self.cursor.fetchall()
            bal1 = str(bal1[0])
            bal1 = int(bal1.strip("\',()"))
            bal1 += amount
            self.cursor.execute(
                "UPDATE amount SET balance ='{}' WHERE account_number = '{}'".format(bal1, account_number))
            # "INSERT INTO amount (balance, account_number) values ('{}', '{}')".format(amount, account_number))
            messagebox.showinfo("Success", "Transfer Successful.")

        else:
            messagebox.showerror("Error", "Account does not exist!")

        self.cursor.execute("SELECT account_number FROM reg_app WHERE username = '{}'".format(test))
        result = self.cursor.fetchall()
        print("result is")
        print(result[0])
        acc_num = str(result[0])
        acc_num = acc_num.strip("\',()")
        self.cursor.execute("SELECT balance FROM amount WHERE account_number = '{}'".format(acc_num))
        results = self.cursor.fetchall()
        print("results is")
        print(results[0])
        bal = str(results[0])
        bal = bal.strip("\',()")
        print("bal is")
        print(bal)
        self.balance.configure(text='''N{}'''.format(bal))
        self.conn.commit()
        # try:
        #     self.cursor.execute("SELECT * FROM reg_bank ORDER BY id DESC LIMIT 1")
        #     result1 = self.cursor.fetchall()
        #     self.conn.commit()
        #     print("ooihh")
        #     if account_number in result1:
        #             messagebox.showinfo("Success", "Transfer Successful.")
        # except ImportMessagebox:

        #

    #
    def active_mtnbutton(self):
        self.mtnbutton.config(relief="sunken")
        self.vmobilebuuton.config(relief="raised")
        self.airtelbutton.config(relief="raised")
        self.globutton.config(relief="raised")

    def active_airtelbutton(self):
        self.airtelbutton.config(relief="sunken")
        self.vmobilebuuton.config(relief="raised")
        self.mtnbutton.config(relief="raised")
        self.globutton.config(relief="raised")

    def active_globutton(self):
        self.globutton.config(relief="sunken")
        self.vmobilebuuton.config(relief="raised")
        self.airtelbutton.config(relief="raised")
        self.mtnbutton.config(relief="raised")

    def active_vmobilebutton(self):
        self.vmobilebuuton.config(relief="sunken")
        self.mtnbutton.config(relief="raised")
        self.airtelbutton.config(relief="raised")
        self.globutton.config(relief="raised")

    def airtime_recharge(self):
        mobile_number = self.mnumentry.get()
        amount = int(self.amountentry.get())
        username = self.Entry1.get()

        mobile_number_pattern = '\\d{11}'
        mobile_number_result = re.match(mobile_number_pattern, mobile_number)

        if not mobile_number_result:
            messagebox.showerror("Error", "Invalid phone number!")
        else:
            self.cursor.execute("SELECT account_number FROM reg_app WHERE username = '{}'".format(username))
            result = self.cursor.fetchone()
            result = str(result)
            result = result.strip("\',()")
            self.cursor.execute("SELECT balance FROM amount WHERE account_number = '{}'".format(result))
            bal = self.cursor.fetchone()
            bal = str(bal)
            bal = int(bal.strip("\',()"))
            if bal > amount:
                bal -= amount
                self.cursor.execute(
                    "UPDATE amount SET balance ='{}' WHERE account_number = '{}'".format(bal, result))
                messagebox.showinfo("Success", "Airtime recharge successful.")
        self.conn.commit()

    def del_account(self):
        time.sleep(0.2)
        account_number = self.delentry.get()
        self.cursor.execute("SELECT * FROM reg_bank ORDER BY id DESC LIMIT 1")
        result = self.cursor.fetchall()
        self.cursor.execute("DELETE FROM reg_bank WHERE Acc_num = '{}'".format(account_number))
        self.cursor.execute("DELETE FROM amount WHERE account_number = '{}'".format(account_number))
        self.cursor.execute("DELETE FROM reg_app WHERE account_number = '{}'".format(account_number))
        self.conn.commit()

        if account_number in result:
            messagebox.showinfo("Success", "Account deleted Successfully.")
        else:
            messagebox.showerror("Error", "Invalid Account number!")

    # command = lambda: self.validation_acc_thread(None)
    def validation_acc_thread(self, event):
        validate_acc_thread = threading.Thread(target=self.validate_acc)
        validate_acc_thread.daemon = True
        validate_acc_thread.start()

    def validation_thread(self, event):
        validate_thread = threading.Thread(target=self.validate)
        validate_thread.daemon = True
        validate_thread.start()

    def authentication_thread(self, event):
        authenticate_thread = threading.Thread(target=self.authenticate)
        authenticate_thread.daemon = True
        authenticate_thread.start()

    def depositing_thread(self, event):
        deeposit_thread = threading.Thread(target=self.deeposit)
        deeposit_thread.daemon = True
        deeposit_thread.start()

    def reset_thread(self, event):
        changepin_thread = threading.Thread(target=self.changepin)
        changepin_thread.daemon = True
        changepin_thread.start()

    def showaccnum_thread(self, event):
        show_acc_num_thread = threading.Thread(target=self.show_acc_num)
        show_acc_num_thread.daemon = True
        show_acc_num_thread.start()

    def balance_thread(self, event):
        show_balance_thread = threading.Thread(target=self.show_balance)
        show_balance_thread.daemon = True
        show_balance_thread.start()

    def Naming_thread(self, event):
        show_name_thread = threading.Thread(target=self.show_name)
        show_name_thread.daemon = True
        show_name_thread.start()

    def transfering_thread(self, event):
        transfers_thread = threading.Thread(target=self.transfers)
        transfers_thread.daemon = True
        transfers_thread.start()

    def get_transaction_info(self):
        my_shelve = shelve.open("usershelf")


if __name__ == '__main__':
    vp_start_gui()