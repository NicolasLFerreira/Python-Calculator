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
	
	# Constructor.
	def __init__(self):

		# Stored value from previous calculations.
		self.result = 0.0

		# Value currently stored for calculation.
		self.operating_value = 0.0

		# Number being currently input by the user.
		self.building_number = ['']

		# If the current number is decimal or not.
		self.decimal = False

		# Switch for radiation operations.
		self.rad_operation = False

		# Enum of the operation currently stored.
		self.current_operation = None

		# Whether to allow the input of an operation.
		self.allow_operation = False

		# Whether it's the first input of the cycle.
		self.first = True

	# Entry method.

	def caller(self, type, id):
		"""Entry point of the class. External methods must call this."""

		output_data = None

		print("call info:", type, id)

		# Calls the respective function for the given input.
		if (type == Type.NUMBER):
			print("num")
			output_data = self.number_call(id)
		elif (type == Type.OPERATION):
			print("oper")
			output_data = self.operation_call(Operation(id))
		elif (type == Type.FUNCTIONALITY):
			print("func")
			output_data = self.functionality_call(Functionality(id))

		# Output.
		return self.output_handler(output_data)
	
	# Input types managers methods.

	def number_call(self, id):
		"""Adds the user input to the self.building_number."""
		
		# Appends the input to the list.
		self.building_number.append(str(id))

		# Allows operations to be performed now that there isn't an empty number.
		self.allow_operation = True

		# Output.
		return OutputData(is_number = True, first = self.first, current_operation = self.current_operation, building_number = self.building_number, result = self.result)
		

	def operation_call(self, type):
		"""Manages operation calls."""

		# Checks to see if it's a operation sign swap or new entry.
		# If it's a new entry, first performs a calculation with the current information.

		# Radiation operations are printed in a special way in the screen.
		if (type == Operation.RAD):
			self.rad_operation = True
		else:
			self.rad_operation = False

		if (self.allow_operation):
			self.allow_operation = False
			self.calculate()
		
		# Assigns the new operation type.
		self.current_operation = type

		# Output.
		return OutputData(is_number = True, first = self.first, current_operation = self.current_operation, building_number = self.building_number, result = self.result)

	def functionality_call(self, type):
		"""Manages functionality calls."""

		# Performs a calculation and returns outputs the result.
		if (type == Functionality.EQUALS and self.current_operation != None):
			return self.equals()
			print("equals")

		# Simply resets the entries.
		elif (type == Functionality.CLEAR):
			self.reset()

		# Deletes the last element of the building_number list, or performs nothing if it's empty.
		elif (type == Functionality.DELETE):
			if (len(self.building_number) > 1):
				if (self.building_number.pop() == '.'):
					self.decimal = False

		# Inverts the sign of the building_number.
		elif (type == Functionality.INVERT):
			if (self.building_number[0] == ''):
				self.building_number[0] = '-'
			else:
				self.building_number[0] = ''

		# Stars the decimal houses in the current number.
		elif (type == Functionality.DEC):
			if (not self.decimal):
				self.building_number.append('.')
				self.decimal = True
				
		# Output.
		return OutputData(is_number = True, first = self.first, rad_operation = self.rad_operation, current_operation = self.current_operation, building_number = self.building_number, result = self.result)

	# Utility methods.

	def equals(self):
		"""Performs only the calculation of the current expression and returns the result."""

		# Checks if the building_number is not empty.
		if (len(self.building_number) > 1):

			self.calculate()

			# Store the output data before it's reseted.
			output_data = OutputData(is_number = True, first = self.first, result = self.result)

			# Converts the self.result to a list.
			list = self.parse()

			self.reset()
		
			# Changes some of the properties.
			self.building_number = list
			self.allow_operation = True
			self.decimal = True

		# Output.
		return OutputData(is_number = True, first = self.first, building_number = self.building_number, result = self.result)

	def parse(self):
		"""Takes the self.result and parses it into a list."""
		number = str(float(self.result))
		list_num = ['']

		for x in number:
		    list_num.append(x)
		return list_num
		

	def calculate(self):
		"""Performs the selected operation on both the self.result and self.current_value. self.rad() is a special case."""

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
		else:
			self.result = self.operating_value

	def wrapper(self):
		"""Converts the building_number value to float, pass it to the operating_value and resets the building_number."""
		self.first = False
		self.operating_value = float("".join(self.building_number))
		self.building_number = ['']
		self.decimal = False
		
	def reset(self):
		"""Sets the properties of the object back to the default values."""
		self.result = 0.0
		self.operating_value = 0.0
		self.building_number = ['']
		self.decimal = False
		self.expression = ""

		self.current_operation = None
		self.allow_operation = False
		self.rad_operation = False
		self.first = True

		print("reset")
	
	# Operations.
	
	def sum(self):
		"""Summation."""
		self.result += self.operating_value
		
	def sub(self):
		"""Subtraction."""
		self.result -= self.operating_value
		
	def mult(self):
		"""Multiplication."""
		self.result *= self.operating_value
		
	def divi(self):
		"""Division."""
		if (self.operating_value != 0.0):
			print(self.operating_value)
			self.result /= self.operating_value
	
	def pow(self):
		"""Exponentiation."""
		self.result **= self.operating_value
		
	def rad(self):
		"""Radiation."""
		self.result **= (1 / self.operating_value)

	# Output.

	def output_handler(self, output_data=None):
		"""Method for processing the data that will be outputted. Takes an object of the class OutputData and returns something based on it."""
		
		# Check to see if the output_data is empty.
		if (output_data == None):
			return "ERROR: empty output data"

		# Number output.
		if (output_data.is_number):
			print("output num")

			# This variable is used in the place of the constant "None". This way I can more
			# easily change the value being used as the checking value and can debug more easily.
			bad_value = "bad_value"

			# Checks the data and prints only the ones that are not empty.
			# Operation sign.
			oper = str(operation_sign()[output_data.current_operation]) if output_data.current_operation != None else bad_value
			# Result.
			num1 = str(output_data.result)
			# Building number.
			num2 = str("".join(output_data.building_number)) if output_data.building_number != [''] else bad_value

			# Debugging only.
			print("oper:", oper)
			print("num1:", num1)
			print("num2:", num2)

			# Lots of if checks to see what output scenario this is, so to avoid having blank data on the screen.
			# First time that something is being inputted.
			if (output_data.first):
				return num2

			# Radiation case.
			if (self.rad_operation):
					if (num2 == bad_value):
						return oper + " " + num1
					else:
						return num2 + " " + num1

			# Normally after a equals.
			elif (oper == bad_value and num2 == bad_value):
				return num1

			# When you only have the result and operation.
			elif (oper != bad_value and num2 == bad_value):
				return (str(output_data.result) + " " + oper)

			# When you have everything.
			elif (oper != bad_value and num2 != bad_value and not output_data.first):
				return num1 + " " + oper + " " + num2

		# Error output.
		print(">ERROR")
		return output_data.error