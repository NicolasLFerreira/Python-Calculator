from tkinter import *
from tkinter import ttk
import tkinter as tk

from Core.Application import Application
from Core.Calculation import Calculation
from enum import *

# Top level widget
root = Tk()

class A(IntEnum):
    x = 1
    y = 2
    z = 3

# Main function. Assembles the code together
def main():
    #a = []
    #a.append(1)
    #a.append(2)
    
    #string = ""
    #for x in a:
    #    string += str(x)

    #print(str(float(string)))

    calc = Calculation()
    app = Application(None, calc, root)
    app.master.title("Calc-o-Lator")
    app.mainloop()

    #print(1 == A.y.real)

main()