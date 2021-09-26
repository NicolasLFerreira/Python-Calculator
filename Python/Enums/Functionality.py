import enum

class Functionality(enum.IntEnum):
    """Enumerator used to define which functionality was called"""
    
    EQUALS = 1
    DELETE = 2
    CLEAR = 3
    DEC = 4