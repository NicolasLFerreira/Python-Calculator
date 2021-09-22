import enum

class Operation(enum.IntEnum):
    """Enumerator used to define which operation was called"""

    ADD = 1
    SUB = 2
    MULT = 3
    DIVI = 4
    POW = 5
    SQRT = 6