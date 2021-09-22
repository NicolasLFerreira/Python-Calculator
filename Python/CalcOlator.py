from tkinter import *
from tkinter import ttk
import tkinter as tk
import math

from Core.Application import Application
from Core.InputProcessing import InputProcessing

# Top level widget
root = Tk()

# Main function. Assembles the code together
def main():
    inprocessing = InputProcessing()
    app = Application(None, inprocessing, root)
    app.master.title("Calc-o-Lator")
    app.mainloop()

main()