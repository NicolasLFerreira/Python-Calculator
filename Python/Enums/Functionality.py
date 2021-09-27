import enum

class Functionality(enum.IntEnum):
    """Enumerator used to define which functionality was called"""
    
    DEC = 1
    EQUALS = 2
    DELETE = 3
    CLEAR = 4