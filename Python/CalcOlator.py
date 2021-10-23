from tkinter import *
from tkinter import ttk
import tkinter as tk

from Core.Application import Application
from Core.Calculation import Calculation
from enum import *

# Top level widget
root = Tk()


# Main function. Assembles the code together
def main():

    calc = Calculation()
    app = Application(None, calc, root)
    app.master.title("Calc-o-Lator")
    app.mainloop()

main()