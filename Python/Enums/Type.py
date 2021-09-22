import enum

class Type(enum.IntEnum):
    """An enumerator used to define whether the input is functionality or calculation member"""

    NUMBER = 1
    OPERATION = 2
    FUNCTIONALITY = 3