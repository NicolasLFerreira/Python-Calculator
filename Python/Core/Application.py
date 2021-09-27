from tkinter import *
from tkinter import ttk
import tkinter as tk
import math

from Enums.Operation import Operation
from Enums.Functionality import Functionality
from Enums.Type import Type

from Misc.Signs import *

# Main class for TKinter object generation
class Application(Frame):
    # inprocessing responds to liskov substitution SOLID principle.
    # Application() will make method calls when input signals are sent
    def __init__(self, master=None, inprocessing=None, root=None):
        Frame.__init__(self, master)

        # Defines the root of the program
        self.root = root

        # Dictionaries for storing the TKinter button objects instances
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

        # Number manager
        self.call = inprocessing

        # Calls the generation methods
        self.generate_elements()

    ####################
    # Element Creation #
    ####################    	

    def generate_elements(self):
        # Number buttons.
        for id in range(1, 10):
            frow = self.formula(id, 3, True, 1)
            fcolumn = self.formula(id, 3, False)
            self.button_number(id, lambda num: print(num), frow, fcolumn)
        
        self.button_number(0, lambda num: print(num), 4, 1)

        # Operation Buttons.
        for id in range(1, 7):
            frow = self.formula(id, 2, True, 1)
            fcolumn = self.formula(id, 2, False, 3)
            print(id, self.operation_sign[id], frow, fcolumn)
            self.button_operations(id, lambda oper: print(oper), frow, fcolumn)

        # Functionality buttons

        self.button_functionality(Functionality.DEC, lambda oper: print(oper), 4,0)
        self.button_functionality(Functionality.EQUALS, lambda oper: print(oper), 4, 2)
        self.button_functionality(Functionality.DELETE, lambda oper: print(oper), 4, 3)
        self.button_functionality(Functionality.CLEAR, lambda oper: print(oper), 4, 4)
        
        # Input.
        self.input = Entry(self.root, font=("Helvetic", int(self.font_base * self.scale_factor), "bold"), width=int(self.width_base * self.scale_factor * 5))
        self.input.grid(row=0, columnspan=5)
        


    ####################
    # Tkinter Elements #
    ####################

    # Base button method.  This serves in order to keep some pattern on how
    # every type of button will behave
    # The parameters are:
    # - An ID for it to be distinguished
    # - A type enum Type
    # - A text which will be printed in the screen
    # - The row
    # - The column
    def base_button(self, index, text, callback, frow, fcolumn):
        id = (index)
        btn = Button(self.root)
        btn["text"] = text 
        btn["command"] = lambda: callback(id)

        # The scale factor of the button.  This is used in order to change its
        # size and that of its contents.
        btn["height"] = int(self.height_base * self.scale_factor)
        btn["width"] = int(self.width_base * self.scale_factor)

        btn.config(font=("Courier", int(self.font_base * self.scale_factor), "bold"))
        btn.grid(row=frow, column=fcolumn)
        return btn

    # For numeric buttons
    def button_number(self, id, callback, frow, fcolumn):
        btn = self.base_button(id, str(id), lambda id: self.call.caller(Type.NUMBER, id), frow, fcolumn)
        self.numbers[id] = btn
    
    # For operation buttons
    def button_operations(self, id, callback, frow, fcolumn):
        btn = self.base_button(id, self.operation_sign[Operation(id)], lambda id: self.call.caller(Type.OPERATION, id), frow, fcolumn)
        self.operations[id] = btn

    # For functionality buttons.  E.g.  equals or delete
    def button_functionality(self, id, callback, frow, fcolumn):
        btn = self.base_button(id, self.functionality_sign[Operation(id)], lambda id: self.call.caller(Type.FUNCTIONALITY, id), frow, fcolumn)
        self.functionalities[id] = btn

    # Method which calculates a position for which the button will be based on
    # given parameters.
    def formula(self, id, factor, isRow=True, fix=0):
        return 4 - (fix + math.floor(abs(id - 1) / factor)) if isRow else fix + (id - 1) % factor
