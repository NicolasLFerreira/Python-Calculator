from tkinter import *
from tkinter import ttk
import tkinter as tk
import math

from Enums.Operation import Operation
from Enums.Functionality import Functionality
from Enums.Type import Type

from Misc.Signs import *

class Application(Frame):
    """Main class of the entire application."""
    def __init__(self, master=None, inprocessing=None, root=None):
        Frame.__init__(self, master)

        # Defines the root of the program.
        self.root = root

        self.root.resizable(width = False, height = False)

        # Dictionaries for storing the TKinter button objects instances.
        self.numbers = {}
        self.operations = {}
        self.functionalities = {}

        # Dictionaries for storing the button's symbols.
        self.functionality_sign = functionality_sign()
        self.operation_sign = operation_sign()
        

        # Size parameters.  Change for resizing each element of the
        # application.
        self.scale_factor = 2
        self.width_base = 3
        self.height_base = 1
        self.font_base = 10

        # Label.
        self.text = tk.StringVar()
        self.label = None

        # Number manager.
        self.call = inprocessing

        # Calls the generation methods.
        self.generate_elements()

    ####################
    # Element Creation #
    ####################    	

    def generate_elements(self):
        """Here is where all the buttons and other TKinter elements are created."""
        # Numeric buttons.
        for id in range(1, 10):
            frow = self.formula(id, 3, True, 1)
            fcolumn = self.formula(id, 3, False)
            self.button_number(id, frow, fcolumn)
        
        self.button_number(0, 4, 1)

        # Operation Buttons.
        for id in range(1, 7):
            frow = self.formula(id, 2, True, 1)
            fcolumn = self.formula(id, 2, False, 3)
            print(id, self.operation_sign[id], frow, fcolumn)
            self.button_operations(id, frow, fcolumn)

        # Functionality buttons.

        self.button_functionality(Functionality.DEC, 4,0)
        self.button_functionality(Functionality.EQUALS, 0, 4)
        self.button_functionality(Functionality.DELETE, 4, 3)
        self.button_functionality(Functionality.CLEAR, 4, 4)
        self.button_functionality(Functionality.INVERT, 4, 2)
        
        # Input
        self.label = Label(self.root, textvariable=self.text, font=("Helvetic", int(self.font_base * self.scale_factor), "bold"), width=int(self.width_base * self.scale_factor * 4))
        self.label.grid(row=0, columnspan=4)
        
    ####################
    # Tkinter Elements #
    ####################

    # Base button method.  This serves in order to keep some pattern on how
    # every type of button will behave
    # The parameters are:
    # - An ID for it to be distinguished
    # - A text which will be printed in the screen
    # - A type enum Type
    # - The row
    # - The column
    def base_button(self, id, text, type, frow, fcolumn):
        """Base button class with elements that all the other buttons in this program will have."""
        # Creates the instance of the button TKinter Element.
        btn = Button(self.root)
        
        # The text of the button.
        btn["text"] = text 
        
        # Call the button_call method
        btn["command"] = lambda: self.button_call(type, id)

        # The scale factor of the button.  This is used in order to change its
        # size and that of its contents.
        btn["height"] = int(self.height_base * self.scale_factor)
        btn["width"] = int(self.width_base * self.scale_factor)

        btn.config(font=("Courier", int(self.font_base * self.scale_factor), "bold"))
        btn.grid(row=frow, column=fcolumn)
        return btn

    def button_number(self, id, frow, fcolumn):
        """For numeric buttons."""
        btn = self.base_button(id, str(id), Type.NUMBER, frow, fcolumn)
        self.numbers[id] = btn
   
    def button_operations(self, id, frow, fcolumn):
        """For operation buttons."""
        btn = self.base_button(id, self.operation_sign[Operation(id)], Type.OPERATION, frow, fcolumn)
        self.operations[id] = btn

    def button_functionality(self, id, frow, fcolumn):
        """For functionality buttons.  E.g.  equals, delete, clear, etc..."""
        btn = self.base_button(id, self.functionality_sign[Operation(id)], Type.FUNCTIONALITY, frow, fcolumn)
        self.functionalities[id] = btn

    ########
    # Misc #
    ########

    def button_call(self, type, id):
        """Calls the calculation class entry point method and calls the output display function."""

        # Calculation entry point.
        output = self.call.caller(type, id)

        # Prints output.
        self.change_text(output)

    def change_text(self, output):
        """Sets the display"""
        print("output:",output)
        self.text.set(str(output))

    def formula(self, id, factor, isRow=True, fix=0):
        """Method which calculates a position for which the button will be based on given parameters."""
        return 4 - (fix + math.floor(abs(id - 1) / factor)) if isRow else fix + (id - 1) % factor
