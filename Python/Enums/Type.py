import enum

class Type(enum.IntEnum):
    """Enumerator used to define which type was called"""

    NUMBER = 1
    OPERATION = 2
    FUNCTIONALITY = 3
    