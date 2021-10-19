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
	""" Everything related to calculation is inside here """
	def __init__(self):
		# Stored value from previous calculations
		self.result = 0.0
		# Value currently stored for calculation
		self.operating_value = 0.0
		# Number being currently input by the user
		self.building_number = []
		# N/A
		self.expression = ""

		# Enum of the operation currently stored
		self.current_operation = None
		# Whether to allow the input of an operation
		self.allow_operation = False
		# Whether it's the first input of the cycle
		self.first = True

	def caller(self, type, id):
		"""Entry point of the class"""

		# Checks what type of button called the function and calls the correspoding method.
		if (type == Type.NUMBER):
			print("num")
			return self.number_call(id)
		elif (type == Type.OPERATION and self.allow_operation):
			print("oper")
			return self.operation_call(Operation(id))
		elif (type == Type.FUNCTIONALITY):
			print("func")
			return self.functionality_call(Functionality(id))
	
	# Input types managers methods

	def number_call(self, id):
		"""Adds the user input to the self.building_number"""
		self.building_number.append(str(id))
		self.allow_operation = True
		return self.output_update(True)

	def operation_call(self, type):
		"""Manages operations"""
		
		self.allow_operation = False
		self.calculate()

		self.current_operation = type
		return self.output_update(True)

	def functionality_call(self, type):
		"""Calls the respective functionality for the given id"""
		if (type == Functionality.EQUALS):
			self.equals()
			print("equals")
			
		elif (type == Functionality.DELETE):
			if (self.building_number.count > 0):
				self.building_number.pop()
		elif (type == Functionality.CLEAR):
			self.reset()

		return self.output_update(True)
	
	# Utility methods
	
	def equals(self):
		self.calculate()
		self.current_operation = None
		self.output_update(True)

		value = self.operating_value

		self.reset()
		self.result = value

	def calculate(self):
		"""The bare minimum code for an operation to be completed"""
		self.wrapper()
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

	def wrapper(self):
		"""Converts the building_number value to float, pass it to the operating_value and resets the building_number"""
		self.first = False
		self.operating_value = float("".join(self.building_number))
		self.building_number = []
		
	def reset(self):
		"""Sets the properties of the object back to the default values"""
		self.result = 0.0
		self.operating_value = 0.0
		self.building_number = []
		self.expression = ""

		self.current_operation = Operation.ADD
		self.allow_operation = False
		self.first = True

		print("RESET")
	
	# Operations
	
	def sum(self):
		self.result += self.operating_value

	def sub(self):
		self.result -= self.operating_value

	def mult(self):
		self.result *= self.operating_value

	def divi(self):
		# Error
		if (self.operating_value == 0.0):
			self.error_handler("Can't divide by zero")
			return
		# Calculate
		self.result /= self.operating_value
	
	def pow(self):
		self.result **= self.operating_value

	def rad(self):
		self.result **= (1 / self.operating_value)

	def error_handler(self, error):
		"""This is called in case that the user's input is invalid for the given operation"""
		self.output_update(False, error)
		self.reset()

	def output_update(self, is_number, error = "Unknown error"):
		"""Outputs the state of the calculation. Can be ea number or error message"""

		# Numeric output
		if (is_number):
			print("output num")
			num = "".join(self.building_number)
			if (self.first):
				return num
			return (str(self.result) + " " + (str(operation_sign()[self.current_operation]) + " " + num))
		# Error
		print("error")
		return error