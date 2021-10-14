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
		self.building_number = ""
		self.expression = ""

		self.current_operation = Operation.ADD
		self.allow_operation = False

	def caller(self, type, id):

		# Checks what type of button called the function and calls the correspoding method.
		if type == Type.NUMBER:
			print("num")
			self.number_call(id)
		elif type == Type.OPERATION and self.allow_operation:
			print("oper")
			self.operation_call(id)
		else:
			print("func")
			return self.functionality_call(id)

		return self.output_update()

	# Adds the user input to the self.building_number as a string for easy management
	def number_call(self, id):
		self.building_number += str(id)
		self.allow_operation = True

	# Manages operations
	def operation_call(self, id):
		
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

		self.current_operation = Operation(id)
	
	# Method for functionality button call
	def functionality_call(self, id):
		self.operation_call(1)
		result = self.result
		self.reset()
	
	# Finishes the building number and sets the current number as a float value.
	def wrapper(self):
		self.current_number = float(self.building_number)
		self.building_number = ""

	# Resets all the values of the class
	def reset(self):
		self.result = 0.0
		self.current_number = 0.0
		self.building_number = ""
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
		self.result /= self.current_number
	
	def pow(self):
		self.result **= self.current_number

	def rad(self):
		self.result **= (1 / self.current_number)

	def output_update(self):
		return (str(self.result) + " " + str(operation_sign()[self.current_operation]) + " " + str(self.building_number))