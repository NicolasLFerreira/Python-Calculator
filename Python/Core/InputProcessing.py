from queue import *

# Main class for processing the given input and operate on it. Works in parallel with the Application() class
class InputProcessing:
    def __init__(self):
        self.calculation = Queue()