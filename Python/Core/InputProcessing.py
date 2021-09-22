# Main class for processing the given input and operate on it. Works in parallel with the Application() class
class InputProcessing:
    def __init__(self):
        # The numeric value of the result of the current calculation
        self.result = 0

        # The current number being built
        self.current_number = ""

        # The calculation numbers in order
        self.numbers = list()

        # The calculation operations in order
        self.operations = list()

    def manage_input(self, type, id):
        if type == Type.NUMBER:
            compose_number(id)
        elif type == Type.OPERATION:
            compose_operation(id)

    def compose_number(number):
        self.current_number += number

    def compose_operation(self, id):
        self.numbers.append(int(self.current_number))
        self.current_number = ""
        self.operations.append(Operation(id))

    # USED FOR TESTING
    def TEST(self, x):
        print(x)
