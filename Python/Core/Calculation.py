from Enums.Functionality import Functionality
from Enums.Operation import Operation
from Enums.Type import Type
from Misc.Signs import *
from math import *

# All the calculation magic happens here
# List of operations that can be performed: 
# - Summation
# - Subtraction
# - Multiplication
# - Division
# - Exponentiation
# - Radiation #
class Calculation:
	""" Manages the object for the calculation """
	def __init__(self):
		
		self.result = 0.0
		self.current_number = 0.0
		self.building_number = []
		self.expression = ""

		self.current_operation = Operation.ADD
		self.allow_operation = False
		self.first = True

	# Externals functions call this one
	def caller(self, type, id):

		# Checks what type of button called the function and calls the correspoding method.
		if (type == Type.NUMBER):
			print("num")
			self.number_call(id)
		elif (type == Type.OPERATION and self.allow_operation):
			print("oper")
			self.operation_call(Operation(id))
		elif (type == Type.FUNCTIONALITY):
			print("func")
			return self.functionality_call(Functionality(id))

		return self.output_update(True)

	# Adds the user input to the self.building_number
	def number_call(self, id):
		self.building_number.append(str(id))
		self.allow_operation = True

	# Manages operations
	def operation_call(self, type):
		
		# Wraps the user input
		self.wrapper()
		
		self.allow_operation = False

		# Calls the respective operation method
		if (self.current_operation == Operation.ADD):
			self.sum()
		elif (self.current_operation == Operation.SUB):
			self.sub()
		elif (self.current_operation == Operation.MULT):
			self.mult()
		elif (self.current_operation == Operation.DIVI):
			self.divi()
		elif (self.current_operation == Operation.POW):
			self.pow()
		elif (self.current_operation == Operation.RAD):
			self.rad()

		self.current_operation = type
	
	# Method for functionality button call
	def functionality_call(self, id):
		if (Functionality(id) == Functionality.EQUALS):
			self.operation_call(int(Operation.ADD))
		elif (Functionality(id) == Functionality.DELETE):
			self.building_number.pop()
		elif (Functionality(id) == Functionality.CLEAR):
			self.reset()

		result = self.result
	
	# 
	# Finishes the building number and sets the current number as a float value.
	def wrapper(self):
		self.first = False
		self.current_number = float("".join(self.building_number))
		self.building_number = []

	# Resets all the values of the class
	def reset(self):
		self.result = 0.0
		self.current_number = 0.0
		self.building_number = []
		self.current_operation = Operation.ADD

		print("RESET")
	
	# Operations
	
	def sum(self):
		self.result += self.current_number

	def sub(self):
		self.result -= self.current_number

	def mult(self):
		self.result *= self.current_number

	def divi(self):
		if (self.current_number == 0):
			self.result = "Can't divide by zero"
		self.result /= self.current_number
	
	def pow(self):
		self.result **= self.current_number

	def rad(self):
		self.result **= (1 / self.current_number)

	# If the user input is invalid for the given operation, this method is called
	def error_handler(self, error):
		self.reset()
		self.output_update(False, error)

	# Ouputs the state of the calculation. Can be a number or error message
	def output_update(self, is_number, error = "None"):

		# Numeric output
		if (is_number):
			num = "".join(self.building_number)
			if (self.first):
				return num
			return (str(self.result) + " " + str(operation_sign()[self.current_operation]) + " " + num)
		# Error
		else:
			return error