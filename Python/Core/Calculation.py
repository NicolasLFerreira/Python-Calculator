from Enums.Functionality import Functionality
from Enums.Operation import Operation
from Enums.Type import Type
from Misc.Signs import *
from math import *

# The class where all the calculation magic happens.
# There are a few concepts that defines how this works.
# The way the calculation works is:
# - The user starts clicking the numeric buttons, which call events which then
# operate all the logic,
#	and the current number being inputted is stored in self.current_number.
# - When the user clicks an operation or the equals functionality button, the
# program wraps up the number,
#   adds to the calc_list the inputted operation, and then initializes a new
#   object for the self.building_number.#
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

	# Method for numeric button call
	def number_call(self, id):
		self.building_number += str(id)
		self.allow_operation = True

	# Method for operation button call
	def operation_call(self, id):
		self.wrapper()
		self.allow_operation = False

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
		return result
	
	# Finishes the building number and sets the current number as a float value.
	def wrapper(self):
		self.current_number = float(self.building_number)
		self.building_number = ""

	# Resets all the values of the class
	def reset(self):
		self.result = 0.0
		self.current_number = 0.0
		self.building_number = ""
		print("RESET")

		self.current_operation = Operation.ADD
	
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