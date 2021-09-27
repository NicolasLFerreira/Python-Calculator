from Enums.Functionality import Functionality
from Enums.Operation import Operation
from Enums.Type import Type
from Misc.Signs import *

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
		
		self.calculation = []
		self.building_number = ""

		# Switch variable used for dis/allowing the input of operations
		self.only_number = True

	def caller(self, type, id):
		if type == Type.NUMBER:
			print("num")
			self.number_call(id)
		elif type == Type.OPERATION:
			print("oper")
			self.operation_call(id)
		else:
			self.functionality_call(id)

	def number_call(self, id):
		print(id)
		self.building_number += str(id)
		self.only_number = False

	def operation_call(self, id):
		if not self.only_number:
			print(id)
			self.wrapper()
			self.calculation.append(Operation(id))
	
	def functionality_call(self, id):
		if not self.calculation == []:
			self.wrapper()
			self.calculate(id)

	def calculate(self, num):
		string = ""
		for x in self.calculation:
			if str(x)[0] == 'O':
				string += operation_sign()[x]
			else:
				string += str(x)
			string += " "
			

		print(string)

		self.calculation = []
		self.building_number = ""

	def wrapper(self):
		self.calculation.append(float(self.building_number))
		self.building_number = ""
		self.only_number = True