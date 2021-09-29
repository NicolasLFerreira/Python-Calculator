from Enums.Operation import Operation
from Enums.Functionality import Functionality

def operation_sign():
    dict = {}

    dict[Operation.ADD] = '+'
    dict[Operation.SUB] = '-'
    dict[Operation.MULT] = '×'
    dict[Operation.DIVI] = '/'
    dict[Operation.POW] = '^'
    dict[Operation.RAD] = '√'

    return dict

def functionality_sign():
    dict = {}

    dict[Functionality.EQUALS] = '='
    dict[Functionality.DELETE] = 'del'
    dict[Functionality.CLEAR] = 'clr'
    dict[Functionality.DEC] = '.'
    dict[Functionality.INVERT] = '-/+'

    return dict