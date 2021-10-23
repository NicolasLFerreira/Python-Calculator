from Enums.Functionality import Functionality
from Enums.Operation import Operation
from Enums.Type import Type
from Core.OutputData import OutputData

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
		self.building_number = ['']
		# If the current number is decimal or not
		self.decimal = False
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

		output_data = None

		# Checks what type of button called the function and calls the correspoding
		# method.
		if (type == Type.NUMBER):
			print("num")
			output_data = self.number_call(id)
		elif (type == Type.OPERATION and self.allow_operation):
			print("oper")
			output_data = self.operation_call(Operation(id))
		elif (type == Type.FUNCTIONALITY):
			print("func")
			output_data = self.functionality_call(Functionality(id))

		if (output_data != None):
			return self.output_update(output_data)
	
	# Input types managers methods

	def number_call(self, id):
		"""Adds the user input to the self.building_number"""
		self.building_number.append(str(id))
		self.allow_operation = True
		return OutputData(is_number = True, first = self.first, current_operation = self.current_operation, building_number = self.building_number, result = self.result)

	def operation_call(self, type):
		"""Manages operations"""
		
		self.allow_operation = False
		self.calculate()
		self.current_operation = type
		return OutputData(is_number = True, first = self.first, current_operation = self.current_operation, building_number = self.building_number, result = self.result)


	def functionality_call(self, type):
		"""Calls the respective functionality for the given id"""
		if (type == Functionality.EQUALS and self.current_operation != None):
			return self.equals()
			print("equals")
		# Resets the entire class
		elif (type == Functionality.CLEAR):
			self.reset()
		# Deletes the last element of the building_number list
		elif (type == Functionality.DELETE):
			if (len(self.building_number) > 1):
				self.building_number.pop()
		# Inverts the sign of the building_number
		elif (type == Functionality.INVERT):
			if (self.building_number[0] == ''):
				self.building_number[0] = '-'
			else:
				self.building_number[0] = ''
		# Makes the building number decimal
		elif (type == Functionality.DEC):
			if (not self.decimal):
				self.building_number.append('.')
				self.decimal = True

		return OutputData(is_number = True, first = self.first, current_operation = self.current_operation, building_number = self.building_number, result = self.result)

	# Utility methods

	def equals(self):
		"""Performs only the calculation of the current expression and returns the result"""
		self.calculate()

		# Store the output data before it's reseted	
		output_data = OutputData(is_number = True, first = self.first, result = self.result)

		# Converts the self.result to a list
		list = self.parse()
		self.reset()
		
		# Corrects some of the properties
		self.building_number = list
		self.allow_operation = True

		return output_data

	def parse(self):
		"""Takes the self.result and parses it into a list"""
		number = str(float(self.result))
		list_num = []

		for x in number:
		    list_num.append(x)
		return list_num
		

	def calculate(self):
		"""Performs the selected operation on both the self.result and self.current_value. self.rad() is a special case"""

		self.wrapper()
		if (self.current_operation == Operation.ADD):
			return self.sum()
		elif (self.current_operation == Operation.SUB):
			return self.sub()
		elif (self.current_operation == Operation.MULT):
			return self.mult()
		elif (self.current_operation == Operation.DIVI):
			return self.divi()
		elif (self.current_operation == Operation.POW):
			return self.pow()
		elif (self.current_operation == Operation.RAD):
			return self.rad()
		else:
			self.result = self.operating_value

	def wrapper(self):
		"""Converts the building_number value to float, pass it to the operating_value and resets the building_number"""
		self.first = False
		self.operating_value = float("".join(self.building_number))
		self.building_number = ['']
		self.decimal = False
		
	def reset(self):
		"""Sets the properties of the object back to the default values"""
		self.result = 0.0
		self.operating_value = 0.0
		self.building_number = ['']
		self.decimal = False
		self.expression = ""

		self.current_operation = None
		self.allow_operation = False
		self.first = True

		print("reset")
	
	# Operations
	
	def sum(self):
		self.result += self.operating_value
		return None

	def sub(self):
		self.result -= self.operating_value
		return None

	def mult(self):
		self.result *= self.operating_value
		return None

	def divi(self):
		# Error
		if (self.operating_value == 0.0):
			return self.error_handler("Can't divide by zero")
		# Calculate
		self.result /= self.operating_value
	
	def pow(self):
		self.result **= self.operating_value
		return None

	def rad(self):
		self.result **= (1 / self.operating_value)
		return None

	def error_handler(self, error):
		"""This is called in case that the user's input is invalid for the given operation"""
		return OutputData(is_number = False, error = error)
		self.reset()

	def output_update(self, output_data=None):
		"""Outputs the state of the calculation. Can be a number or error message"""

		if (output_data == None):
			return "No output data given"

		# Numeric output
		if (output_data.is_number):
			print("output num")

			# Checks the data and prints only the ones that are not empty
			oper = str(operation_sign()[output_data.current_operation]) if output_data.current_operation != None else None
			num1 = str(output_data.result)
			num2 = "".join(output_data.building_number) if output_data.building_number != [] else None

			if (output_data.first):
				return num2

			elif (oper == None and num2 == None):
				return num1

			elif (oper != None and num2 == None):
				return (str(output_data.result) + " " + oper)

			elif (oper != None and num2 != None and not output_data.first):
				return num1 + " " + oper + " " + num2

		# Error output
		print("Super Idol的笑容 都没你的甜 八月正午的阳光 都没你耀眼 热爱 105 °C的你 滴滴清纯的蒸馏水")
		return output_data.error