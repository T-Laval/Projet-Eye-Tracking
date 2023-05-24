import tkthread
# need pip install
import webbrowser
import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import *
import threading
import time
import mouse
import csv

tkthread.patch()

# Initiate BDD
with open('bdd.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    liste_mots = []
    for row in reader:
        liste_mots.append(row[1])

key = tk.Tk()

key.title('On Screen Keyboard')

key.geometry('1385x320')  # Window size
key.maxsize(width=1385, height=320)
key.minsize(width=480, height=110)

style = ttk.Style()
key.configure(bg='gray27')
style.configure('TButton', background='gray21')
style.configure('TButton', foreground='white')

theme = "light"

Grid.rowconfigure(key, 0, weight=1)
Grid.columnconfigure(key, 0, weight=1)
Grid.rowconfigure(key, 1, weight=1)
Grid.columnconfigure(key, 1, weight=1)
Grid.rowconfigure(key, 2, weight=1)
Grid.columnconfigure(key, 2, weight=1)
Grid.rowconfigure(key, 3, weight=1)
Grid.columnconfigure(key, 3, weight=1)
Grid.rowconfigure(key, 4, weight=1)
Grid.columnconfigure(key, 4, weight=1)
Grid.rowconfigure(key, 5, weight=1)
Grid.columnconfigure(key, 5, weight=1)
Grid.columnconfigure(key, 6, weight=1)
Grid.columnconfigure(key, 7, weight=1)
Grid.columnconfigure(key, 8, weight=1)
Grid.columnconfigure(key, 9, weight=1)
Grid.columnconfigure(key, 10, weight=1)
Grid.columnconfigure(key, 11, weight=1)
Grid.columnconfigure(key, 12, weight=1)
Grid.columnconfigure(key, 13, weight=1)

# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key, state='readonly', textvariable=equation)
Dis_entry.grid(rowspan=1, columnspan=100, ipadx=700, ipady=20, sticky="NSEW")

# showing all data in display
exp = " "
is_shift = False


# Necessary functions


class hover_timer:

    def __init__(self, widget, text, delay=2.0):
        self.wind, self.cancel_var, self.widget, self.text, self.active, self.delay = None, False, widget, text, False, delay
        threading.Thread(target=self.start_timer).start()

    def start_timer(self):
        self.active = True
        # time.sleep (self.delay)
        time.sleep(1.0)
        # if not self.cancel_var :
        if not self.cancel_var:
            mouse.click('left')
            print("3seconds IN")
        self.active = False

    def delayed_stop(self):
        while self.active: time.sleep(0.05)
        if self.wind:
            self.wind.destroy()
            self.wind = None

    def cancel(self):
        self.cancel_var = True
        if not self.wind:
            threading.Thread(target=self.delayed_stop).start()
        else:
            self.wind.destroy()
            self.wind = None


h = None


def start_help(event):
    # Create a new help timer
    global h
    h = hover_timer(event.widget, "This is some additional information.", 0.5)


def end_help(event):
    # If therre is one, end the help timer
    print(trouver_mot_plus_proche(exp, liste_mots))
    if h: h.cancel()


def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def Backspace():
    global exp
    exp = exp[:-1]
    equation.set(exp)


def Shift():
    global is_shift
    is_shift = not is_shift
    display()


def Clear():
    global exp
    exp = " "
    equation.set(exp)


def Search():
    global exp
    url = "https://www.google.com.tr/search?q={}".format(exp)
    webbrowser.open_new_tab(url)

def infinite_loop():
    """
    Boucle chaque seconde pour appuyer sur F11. Nécessaire avec caméra Tobii
    """
    pyautogui.press('f11')
    key.after(1000,infinite_loop)

key.after(5000,infinite_loop)

def Theme():
    global theme
    if theme == "dark":
        key.configure(bg='gray27')
        style.configure('TButton', background='gray21')
        style.configure('TButton', foreground='white')
        theme = "light"
    elif theme == "light":
        key.configure(bg='gray99')
        style.configure('TButton', background='azure')
        style.configure('TButton', foreground='black')
        theme = "dark"


def display():
    if (is_shift):
        # Adding keys line wise
        # First Line Button
        tilda = ttk.Button(key, text='~', width=6, command=lambda: press('~'))
        tilda.grid(row=1, column=0, ipadx=6, ipady=10, sticky="NSEW")
        tilda.bind("<Enter>", start_help)
        tilda.bind("<Leave>", end_help)

        num1 = ttk.Button(key, text='!', width=6, command=lambda: press('!'))
        num1.grid(row=1, column=1, ipadx=6, ipady=10, sticky="NSEW")
        num1.bind("<Enter>", start_help)
        num1.bind("<Leave>", end_help)

        num2 = ttk.Button(key, text='@', width=6, command=lambda: press('@'))
        num2.grid(row=1, column=2, ipadx=6, ipady=10, sticky="NSEW")
        num2.bind("<Enter>", start_help)
        num2.bind("<Leave>", end_help)

        num3 = ttk.Button(key, text='#', width=6, command=lambda: press('#'))
        num3.grid(row=1, column=3, ipadx=6, ipady=10, sticky="NSEW")
        num3.bind("<Enter>", start_help)
        num3.bind("<Leave>", end_help)

        num4 = ttk.Button(key, text='$', width=6, command=lambda: press('$'))
        num4.grid(row=1, column=4, ipadx=6, ipady=10, sticky="NSEW")
        num4.bind("<Enter>", start_help)
        num4.bind("<Leave>", end_help)

        num5 = ttk.Button(key, text='%', width=6, command=lambda: press('%'))
        num5.grid(row=1, column=5, ipadx=6, ipady=10, sticky="NSEW")
        num5.bind("<Enter>", start_help)
        num5.bind("<Leave>", end_help)

        num6 = ttk.Button(key, text='^', width=6, command=lambda: press('^'))
        num6.grid(row=1, column=6, ipadx=6, ipady=10, sticky="NSEW")
        num6.bind("<Enter>", start_help)
        num6.bind("<Leave>", end_help)

        num7 = ttk.Button(key, text='&', width=6, command=lambda: press('&'))
        num7.grid(row=1, column=7, ipadx=6, ipady=10, sticky="NSEW")
        num7.bind("<Enter>", start_help)
        num7.bind("<Leave>", end_help)

        num8 = ttk.Button(key, text='*', width=6, command=lambda: press('*'))
        num8.grid(row=1, column=8, ipadx=6, ipady=10, sticky="NSEW")
        num8.bind("<Enter>", start_help)
        num8.bind("<Leave>", end_help)

        num9 = ttk.Button(key, text='(', width=6, command=lambda: press('('))
        num9.grid(row=1, column=9, ipadx=6, ipady=10, sticky="NSEW")
        num9.bind("<Enter>", start_help)
        num9.bind("<Leave>", end_help)

        num0 = ttk.Button(key, text=')', width=6, command=lambda: press(')'))
        num0.grid(row=1, column=10, ipadx=6, ipady=10, sticky="NSEW")
        num0.bind("<Enter>", start_help)
        num0.bind("<Leave>", end_help)

        under = ttk.Button(key, text='_', width=6, command=lambda: press('_'))
        under.grid(row=1, column=11, ipadx=6, ipady=10, sticky="NSEW")
        under.bind("<Enter>", start_help)
        under.bind("<Leave>", end_help)

        plus = ttk.Button(key, text='+', width=6, command=lambda: press('+'))
        plus.grid(row=1, column=12, ipadx=6, ipady=10, sticky="NSEW")
        plus.bind("<Enter>", start_help)
        plus.bind("<Leave>", end_help)

        backspace = ttk.Button(
            key, text='<---', width=6, command=Backspace)
        backspace.grid(row=1, column=13, ipadx=6, ipady=10, sticky="NSEW")

        # Second Line Buttons

        tab_button = ttk.Button(key, text='Tab', width=6,
                                command=lambda: press('\t'))
        tab_button.grid(row=2, column=0, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        tab_button.bind("<Enter>", start_help)
        tab_button.bind("<Leave>", end_help)

        A = ttk.Button(key, text='A', width=6, command=lambda: press('A'))
        A.grid(row=2, column=2, ipadx=6, ipady=10, sticky="NSEW")
        A.bind("<Enter>", start_help)
        A.bind("<Leave>", end_help)

        Z = ttk.Button(key, text='Z', width=6, command=lambda: press('Z'))
        Z.grid(row=2, column=3, ipadx=6, ipady=10, sticky="NSEW")
        Z.bind("<Enter>", start_help)
        Z.bind("<Leave>", end_help)

        E = ttk.Button(key, text='E', width=6, command=lambda: press('E'))
        E.grid(row=2, column=4, ipadx=6, ipady=10, sticky="NSEW")
        E.bind("<Enter>", start_help)
        E.bind("<Leave>", end_help)

        R = ttk.Button(key, text='R', width=6, command=lambda: press('R'))
        R.grid(row=2, column=5, ipadx=6, ipady=10, sticky="NSEW")
        R.bind("<Enter>", start_help)
        R.bind("<Leave>", end_help)

        T = ttk.Button(key, text='T', width=6, command=lambda: press('T'))
        T.grid(row=2, column=6, ipadx=6, ipady=10, sticky="NSEW")
        T.bind("<Enter>", start_help)
        T.bind("<Leave>", end_help)

        Y = ttk.Button(key, text='Y', width=6, command=lambda: press('Y'))
        Y.grid(row=2, column=7, ipadx=6, ipady=10, sticky="NSEW")
        Y.bind("<Enter>", start_help)
        Y.bind("<Leave>", end_help)

        U = ttk.Button(key, text='U', width=6, command=lambda: press('U'))
        U.grid(row=2, column=8, ipadx=6, ipady=10, sticky="NSEW")
        U.bind("<Enter>", start_help)
        U.bind("<Leave>", end_help)

        I = ttk.Button(key, text='I', width=6, command=lambda: press('I'))
        I.grid(row=2, column=9, ipadx=6, ipady=10, sticky="NSEW")
        I.bind("<Enter>", start_help)
        I.bind("<Leave>", end_help)

        O = ttk.Button(key, text='O', width=6, command=lambda: press('O'))
        O.grid(row=2, column=10, ipadx=6, ipady=10, sticky="NSEW")
        O.bind("<Enter>", start_help)
        O.bind("<Leave>", end_help)

        P = ttk.Button(key, text='P', width=6, command=lambda: press('P'))
        P.grid(row=2, column=11, ipadx=6, ipady=10, sticky="NSEW")
        P.bind("<Enter>", start_help)
        P.bind("<Leave>", end_help)

        curly_l = ttk.Button(
            key, text='{', width=6, command=lambda: press('{'))
        curly_l.grid(row=2, column=12, ipadx=6, ipady=10, sticky="NSEW")
        curly_l.bind("<Enter>", start_help)
        curly_l.bind("<Leave>", end_help)

        curly_r = ttk.Button(key, text='}', width=6,
                             command=lambda: press('}'))
        curly_r.grid(row=2, column=13, ipadx=6, ipady=10, sticky="NSEW")
        curly_r.bind("<Enter>", start_help)
        curly_r.bind("<Leave>", end_help)

        # Third Line Buttons
        shift = ttk.Button(key, text='Shift', width=6, command=Shift)
        shift.grid(row=3, column=0, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        shift.bind("<Enter>", start_help)
        shift.bind("<Leave>", end_help)

        Q = ttk.Button(key, text='Q', width=6, command=lambda: press('Q'))
        Q.grid(row=3, column=2, ipadx=6, ipady=10, sticky="NSEW")
        Q.bind("<Enter>", start_help)
        Q.bind("<Leave>", end_help)

        S = ttk.Button(key, text='S', width=6, command=lambda: press('S'))
        S.grid(row=3, column=3, ipadx=6, ipady=10, sticky="NSEW")
        S.bind("<Enter>", start_help)
        S.bind("<Leave>", end_help)

        D = ttk.Button(key, text='D', width=6, command=lambda: press('D'))
        D.grid(row=3, column=4, ipadx=6, ipady=10, sticky="NSEW")
        D.bind("<Enter>", start_help)
        D.bind("<Leave>", end_help)

        F = ttk.Button(key, text='F', width=6, command=lambda: press('F'))
        F.grid(row=3, column=5, ipadx=6, ipady=10, sticky="NSEW")
        F.bind("<Enter>", start_help)
        F.bind("<Leave>", end_help)

        G = ttk.Button(key, text='G', width=6, command=lambda: press('G'))
        G.grid(row=3, column=6, ipadx=6, ipady=10, sticky="NSEW")
        G.bind("<Enter>", start_help)
        G.bind("<Leave>", end_help)

        H = ttk.Button(key, text='H', width=6, command=lambda: press('H'))
        H.grid(row=3, column=7, ipadx=6, ipady=10, sticky="NSEW")
        H.bind("<Enter>", start_help)
        H.bind("<Leave>", end_help)

        J = ttk.Button(key, text='J', width=6, command=lambda: press('J'))
        J.grid(row=3, column=8, ipadx=6, ipady=10, sticky="NSEW")
        J.bind("<Enter>", start_help)
        J.bind("<Leave>", end_help)

        K = ttk.Button(key, text='K', width=6, command=lambda: press('K'))
        K.grid(row=3, column=9, ipadx=6, ipady=10, sticky="NSEW")
        K.bind("<Enter>", start_help)
        K.bind("<Leave>", end_help)

        L = ttk.Button(key, text='L', width=6, command=lambda: press('L'))
        L.grid(row=3, column=10, ipadx=6, ipady=10, sticky="NSEW")
        L.bind("<Enter>", start_help)
        L.bind("<Leave>", end_help)

        colon = ttk.Button(key, text=':', width=6,
                           command=lambda: press(':'))
        colon.grid(row=3, column=11, ipadx=6, ipady=10, sticky="NSEW")
        colon.bind("<Enter>", start_help)
        colon.bind("<Leave>", end_help)

        quotation = ttk.Button(key, text='"', width=6,
                               command=lambda: press('"'))
        quotation.grid(row=3, column=12, ipadx=6, ipady=10, sticky="NSEW")
        quotation.bind("<Enter>", start_help)
        quotation.bind("<Leave>", end_help)

        pipe = ttk.Button(key, text='|', width=6, command=lambda: press('|'))
        pipe.grid(row=3, column=13, ipadx=6, ipady=10, sticky="NSEW")
        pipe.bind("<Enter>", start_help)
        pipe.bind("<Leave>", end_help)

        # Fourth line Buttons
        theme = ttk.Button(key, text='Theme', width=6, command=Theme)
        theme.grid(row=4, column=0, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        theme.bind("<Enter>", start_help)
        theme.bind("<Leave>", end_help)

        W = ttk.Button(key, text='W', width=6, command=lambda: press('W'))
        W.grid(row=4, column=2, ipadx=6, ipady=10, sticky="NSEW")
        W.bind("<Enter>", start_help)
        W.bind("<Leave>", end_help)

        X = ttk.Button(key, text='X', width=6, command=lambda: press('X'))
        X.grid(row=4, column=3, ipadx=6, ipady=10, sticky="NSEW")
        X.bind("<Enter>", start_help)
        X.bind("<Leave>", end_help)

        C = ttk.Button(key, text='C', width=6, command=lambda: press('C'))
        C.grid(row=4, column=4, ipadx=6, ipady=10, sticky="NSEW")
        C.bind("<Enter>", start_help)
        C.bind("<Leave>", end_help)

        V = ttk.Button(key, text='V', width=6, command=lambda: press('V'))
        V.grid(row=4, column=5, ipadx=6, ipady=10, sticky="NSEW")
        V.bind("<Enter>", start_help)
        V.bind("<Leave>", end_help)

        B = ttk.Button(key, text='B', width=6, command=lambda: press('B'))
        B.grid(row=4, column=6, ipadx=6, ipady=10, sticky="NSEW")
        B.bind("<Enter>", start_help)
        B.bind("<Leave>", end_help)

        N = ttk.Button(key, text='N', width=6, command=lambda: press('N'))
        N.grid(row=4, column=7, ipadx=6, ipady=10, sticky="NSEW")
        N.bind("<Enter>", start_help)
        N.bind("<Leave>", end_help)

        M = ttk.Button(key, text='M', width=6, command=lambda: press('M'))
        M.grid(row=4, column=8, ipadx=6, ipady=10, sticky="NSEW")
        M.bind("<Enter>", start_help)
        M.bind("<Leave>", end_help)

        ang_l = ttk.Button(key, text='<', width=6, command=lambda: press('<'))
        ang_l.grid(row=4, column=9, ipadx=6, ipady=10, sticky="NSEW")
        ang_l.bind("<Enter>", start_help)
        ang_l.bind("<Leave>", end_help)

        ang_r = ttk.Button(key, text='>', width=6, command=lambda: press('>'))
        ang_r.grid(row=4, column=10, ipadx=6, ipady=10, sticky="NSEW")
        ang_r.bind("<Enter>", start_help)
        ang_r.bind("<Leave>", end_help)

        question = ttk.Button(key, text='?', width=6,
                              command=lambda: press('?'))
        question.grid(row=4, column=11, ipadx=6, ipady=10, sticky="NSEW")
        question.bind("<Enter>", start_help)
        question.bind("<Leave>", end_help)

        clear = ttk.Button(key, text='Clear', width=6, command=Clear)
        clear.grid(row=4, column=12, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        clear.bind("<Enter>", start_help)
        clear.bind("<Leave>", end_help)

        # Fifth Line Buttons

        space = ttk.Button(key, text='Space', width=6,
                           command=lambda: press(' '))
        space.grid(row=5, column=2, columnspan=8, ipadx=350, ipady=10, sticky="NSEW")
        space.bind("<Enter>", start_help)
        space.bind("<Leave>", end_help)

        enter = ttk.Button(key, text='Enter', width=6,
                           command=Search)
        enter.grid(row=5, column=12, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        enter.bind("<Enter>", start_help)
        enter.bind("<Leave>", end_help)
        key.mainloop()
    else:
        # Adding keys line wise
        # First Line Button
        tick = ttk.Button(key, text='`', width=6, command=lambda: press('`'))
        tick.grid(row=1, column=0, ipadx=6, ipady=10, sticky="NSEW")
        tick.bind("<Enter>", start_help)
        tick.bind("<Leave>", end_help)

        num1 = ttk.Button(key, text='1', width=6, command=lambda: press('1'))
        num1.grid(row=1, column=1, ipadx=6, ipady=10, sticky="NSEW")
        num1.bind("<Enter>", start_help)
        num1.bind("<Leave>", end_help)

        num2 = ttk.Button(key, text='2', width=6, command=lambda: press('2'))
        num2.grid(row=1, column=2, ipadx=6, ipady=10, sticky="NSEW")
        num2.bind("<Enter>", start_help)
        num2.bind("<Leave>", end_help)

        num3 = ttk.Button(key, text='3', width=6, command=lambda: press('3'))
        num3.grid(row=1, column=3, ipadx=6, ipady=10, sticky="NSEW")
        num3.bind("<Enter>", start_help)
        num3.bind("<Leave>", end_help)

        num4 = ttk.Button(key, text='4', width=6, command=lambda: press('4'))
        num4.grid(row=1, column=4, ipadx=6, ipady=10, sticky="NSEW")
        num4.bind("<Enter>", start_help)
        num4.bind("<Leave>", end_help)

        num5 = ttk.Button(key, text='5', width=6, command=lambda: press('5'))
        num5.grid(row=1, column=5, ipadx=6, ipady=10, sticky="NSEW")
        num5.bind("<Enter>", start_help)
        num5.bind("<Leave>", end_help)

        num6 = ttk.Button(key, text='6', width=6, command=lambda: press('6'))
        num6.grid(row=1, column=6, ipadx=6, ipady=10, sticky="NSEW")
        num6.bind("<Enter>", start_help)
        num6.bind("<Leave>", end_help)

        num7 = ttk.Button(key, text='7', width=6, command=lambda: press('7'))
        num7.grid(row=1, column=7, ipadx=6, ipady=10, sticky="NSEW")
        num7.bind("<Enter>", start_help)
        num7.bind("<Leave>", end_help)

        num8 = ttk.Button(key, text='8', width=6, command=lambda: press('8'))
        num8.grid(row=1, column=8, ipadx=6, ipady=10, sticky="NSEW")
        num8.bind("<Enter>", start_help)
        num8.bind("<Leave>", end_help)

        num9 = ttk.Button(key, text='9', width=6, command=lambda: press('9'))
        num9.grid(row=1, column=9, ipadx=6, ipady=10, sticky="NSEW")
        num9.bind("<Enter>", start_help)
        num9.bind("<Leave>", end_help)

        num0 = ttk.Button(key, text='0', width=6, command=lambda: press('0'))
        num0.grid(row=1, column=10, ipadx=6, ipady=10, sticky="NSEW")
        num0.bind("<Enter>", start_help)
        num0.bind("<Leave>", end_help)

        minus = ttk.Button(key, text='-', width=6, command=lambda: press('-'))
        minus.grid(row=1, column=11, ipadx=6, ipady=10, sticky="NSEW")
        minus.bind("<Enter>", start_help)
        minus.bind("<Leave>", end_help)

        equal = ttk.Button(key, text='=', width=6, command=lambda: press('='))
        equal.grid(row=1, column=12, ipadx=6, ipady=10, sticky="NSEW")
        equal.bind("<Enter>", start_help)
        equal.bind("<Leave>", end_help)

        backspace = ttk.Button(
            key, text='<---', width=6, command=Backspace)
        backspace.grid(row=1, column=13, ipadx=6, ipady=10, sticky="NSEW")
        backspace.bind("<Enter>", start_help)
        backspace.bind("<Leave>", end_help)

        # Second Line Buttons

        tab_button = ttk.Button(key, text='Tab', width=6,
                                command=lambda: press('\t'))
        tab_button.grid(row=2, column=0, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        backspace.bind("<Enter>", start_help)
        backspace.bind("<Leave>", end_help)

        A = ttk.Button(key, text='a', width=6, command=lambda: press('a'))
        A.grid(row=2, column=2, ipadx=6, ipady=10, sticky="NSEW")
        A.bind("<Enter>", start_help)
        A.bind("<Leave>", end_help)

        Z = ttk.Button(key, text='z', width=6, command=lambda: press('z'))
        Z.grid(row=2, column=3, ipadx=6, ipady=10, sticky="NSEW")
        Z.bind("<Enter>", start_help)
        Z.bind("<Leave>", end_help)

        E = ttk.Button(key, text='e', width=6, command=lambda: press('e'))
        E.grid(row=2, column=4, ipadx=6, ipady=10, sticky="NSEW")
        E.bind("<Enter>", start_help)
        E.bind("<Leave>", end_help)

        R = ttk.Button(key, text='r', width=6, command=lambda: press('r'))
        R.grid(row=2, column=5, ipadx=6, ipady=10, sticky="NSEW")
        R.bind("<Enter>", start_help)
        R.bind("<Leave>", end_help)

        T = ttk.Button(key, text='t', width=6, command=lambda: press('t'))
        T.grid(row=2, column=6, ipadx=6, ipady=10, sticky="NSEW")
        T.bind("<Enter>", start_help)
        T.bind("<Leave>", end_help)

        Y = ttk.Button(key, text='y', width=6, command=lambda: press('y'))
        Y.grid(row=2, column=7, ipadx=6, ipady=10, sticky="NSEW")
        Y.bind("<Enter>", start_help)
        Y.bind("<Leave>", end_help)

        U = ttk.Button(key, text='u', width=6, command=lambda: press('u'))
        U.grid(row=2, column=8, ipadx=6, ipady=10, sticky="NSEW")
        U.bind("<Enter>", start_help)
        U.bind("<Leave>", end_help)

        I = ttk.Button(key, text='i', width=6, command=lambda: press('i'))
        I.grid(row=2, column=9, ipadx=6, ipady=10, sticky="NSEW")
        I.bind("<Enter>", start_help)
        I.bind("<Leave>", end_help)

        O = ttk.Button(key, text='o', width=6, command=lambda: press('o'))
        O.grid(row=2, column=10, ipadx=6, ipady=10, sticky="NSEW")
        O.bind("<Enter>", start_help)
        O.bind("<Leave>", end_help)

        P = ttk.Button(key, text='p', width=6, command=lambda: press('p'))
        P.grid(row=2, column=11, ipadx=6, ipady=10, sticky="NSEW")
        P.bind("<Enter>", start_help)
        P.bind("<Leave>", end_help)

        sq_l = ttk.Button(key, text='[', width=6, command=lambda: press('['))
        sq_l.grid(row=2, column=12, ipadx=6, ipady=10, sticky="NSEW")
        sq_l.bind("<Enter>", start_help)
        sq_l.bind("<Leave>", end_help)

        sq_r = ttk.Button(key, text=']', width=6, command=lambda: press(']'))
        sq_r.grid(row=2, column=13, ipadx=6, ipady=10, sticky="NSEW")
        sq_r.bind("<Enter>", start_help)
        sq_r.bind("<Leave>", end_help)

        # Third Line Buttons

        shift = ttk.Button(key, text='Shift', width=6, command=Shift)
        shift.grid(row=3, column=0, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        shift.bind("<Enter>", start_help)
        shift.bind("<Leave>", end_help)

        Q = ttk.Button(key, text='q', width=6, command=lambda: press('q'))
        Q.grid(row=3, column=2, ipadx=6, ipady=10, sticky="NSEW")
        Q.bind("<Enter>", start_help)
        Q.bind("<Leave>", end_help)

        S = ttk.Button(key, text='s', width=6, command=lambda: press('s'))
        S.grid(row=3, column=3, ipadx=6, ipady=10, sticky="NSEW")
        S.bind("<Enter>", start_help)
        S.bind("<Leave>", end_help)

        D = ttk.Button(key, text='d', width=6, command=lambda: press('d'))
        D.grid(row=3, column=4, ipadx=6, ipady=10, sticky="NSEW")
        D.bind("<Enter>", start_help)
        D.bind("<Leave>", end_help)

        F = ttk.Button(key, text='f', width=6, command=lambda: press('f'))
        F.grid(row=3, column=5, ipadx=6, ipady=10, sticky="NSEW")
        F.bind("<Enter>", start_help)
        F.bind("<Leave>", end_help)

        G = ttk.Button(key, text='g', width=6, command=lambda: press('g'))
        G.grid(row=3, column=6, ipadx=6, ipady=10, sticky="NSEW")
        G.bind("<Enter>", start_help)
        G.bind("<Leave>", end_help)

        H = ttk.Button(key, text='h', width=6, command=lambda: press('h'))
        H.grid(row=3, column=7, ipadx=6, ipady=10, sticky="NSEW")
        H.bind("<Enter>", start_help)
        H.bind("<Leave>", end_help)

        J = ttk.Button(key, text='j', width=6, command=lambda: press('j'))
        J.grid(row=3, column=8, ipadx=6, ipady=10, sticky="NSEW")
        J.bind("<Enter>", start_help)
        J.bind("<Leave>", end_help)

        K = ttk.Button(key, text='k', width=6, command=lambda: press('k'))
        K.grid(row=3, column=9, ipadx=6, ipady=10, sticky="NSEW")
        K.bind("<Enter>", start_help)
        K.bind("<Leave>", end_help)

        L = ttk.Button(key, text='l', width=6, command=lambda: press('l'))
        L.grid(row=3, column=10, ipadx=6, ipady=10, sticky="NSEW")
        L.bind("<Enter>", start_help)
        L.bind("<Leave>", end_help)

        semi_co = ttk.Button(key, text=';', width=6,
                             command=lambda: press(';'))
        semi_co.grid(row=3, column=11, ipadx=6, ipady=10, sticky="NSEW")
        semi_co.bind("<Enter>", start_help)
        semi_co.bind("<Leave>", end_help)

        quotation = ttk.Button(key, text="'", width=6,
                               command=lambda: press('"'))
        quotation.grid(row=3, column=12, ipadx=6, ipady=10, sticky="NSEW")
        quotation.bind("<Enter>", start_help)
        quotation.bind("<Leave>", end_help)

        back_slash = ttk.Button(key, text='\\', width=6,
                                command=lambda: press('\\'))
        back_slash.grid(row=3, column=13, ipadx=6, ipady=10, sticky="NSEW")
        back_slash.bind("<Enter>", start_help)
        back_slash.bind("<Leave>", end_help)

        # Fourth line Buttons

        theme = ttk.Button(key, text='Theme', width=6, command=Theme)
        theme.grid(row=4, column=0, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        theme.bind("<Enter>", start_help)
        theme.bind("<Leave>", end_help)

        W = ttk.Button(key, text='w', width=6, command=lambda: press('w'))
        W.grid(row=4, column=2, ipadx=6, ipady=10, sticky="NSEW")
        W.bind("<Enter>", start_help)
        W.bind("<Leave>", end_help)

        X = ttk.Button(key, text='x', width=6, command=lambda: press('x'))
        X.grid(row=4, column=3, ipadx=6, ipady=10, sticky="NSEW")
        X.bind("<Enter>", start_help)
        X.bind("<Leave>", end_help)

        C = ttk.Button(key, text='c', width=6, command=lambda: press('c'))
        C.grid(row=4, column=4, ipadx=6, ipady=10, sticky="NSEW")
        C.bind("<Enter>", start_help)
        C.bind("<Leave>", end_help)

        V = ttk.Button(key, text='v', width=6, command=lambda: press('v'))
        V.grid(row=4, column=5, ipadx=6, ipady=10, sticky="NSEW")
        V.bind("<Enter>", start_help)
        V.bind("<Leave>", end_help)

        B = ttk.Button(key, text='b', width=6, command=lambda: press('b'))
        B.grid(row=4, column=6, ipadx=6, ipady=10, sticky="NSEW")
        B.bind("<Enter>", start_help)
        B.bind("<Leave>", end_help)

        N = ttk.Button(key, text='n', width=6, command=lambda: press('n'))
        N.grid(row=4, column=7, ipadx=6, ipady=10, sticky="NSEW")
        N.bind("<Enter>", start_help)
        N.bind("<Leave>", end_help)

        M = ttk.Button(key, text='m', width=6, command=lambda: press('m'))
        M.grid(row=4, column=8, ipadx=6, ipady=10, sticky="NSEW")
        M.bind("<Enter>", start_help)
        M.bind("<Leave>", end_help)

        comma = ttk.Button(key, text=',', width=6, command=lambda: press(','))
        comma.grid(row=4, column=9, ipadx=6, ipady=10, sticky="NSEW")
        comma.bind("<Enter>", start_help)
        comma.bind("<Leave>", end_help)

        dot = ttk.Button(key, text='.', width=6, command=lambda: press('.'))
        dot.grid(row=4, column=10, ipadx=6, ipady=10, sticky="NSEW")
        dot.bind("<Enter>", start_help)
        dot.bind("<Leave>", end_help)

        slash = ttk.Button(key, text='/', width=6, command=lambda: press('/'))
        slash.grid(row=4, column=11, ipadx=6, ipady=10, sticky="NSEW")
        slash.bind("<Enter>", start_help)
        slash.bind("<Leave>", end_help)

        clear = ttk.Button(key, text='Clear', width=6, command=Clear)
        clear.grid(row=4, column=12, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        clear.bind("<Enter>", start_help)
        clear.bind("<Leave>", end_help)

        # Fifth Line Buttons

        space = ttk.Button(key, text='Space', width=6,
                           command=lambda: press(' '))
        space.grid(row=5, column=2, columnspan=8, ipadx=350, ipady=10, sticky="NSEW")
        space.bind("<Enter>", start_help)
        space.bind("<Leave>", end_help)
        enter = ttk.Button(key, text='Enter', width=6,
                           command=Search)
        enter.grid(row=5, column=12, columnspan=2, ipadx=55, ipady=10, sticky="NSEW")
        enter.bind("<Enter>", start_help)
        enter.bind("<Leave>", end_help)
        key.mainloop()


# Recherche de mots
import Levenshtein


def trouver_mot_plus_proche(mot, liste_mots):
    distance_min = float('inf')
    mot_plus_proche = ""

    for mot_liste in liste_mots:
        distance = Levenshtein.distance(mot, mot_liste)
        if distance < distance_min:
            distance_min = distance
            mot_plus_proche = mot_liste

    return mot_plus_proche


display()
