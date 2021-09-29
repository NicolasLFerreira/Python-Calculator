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

		self.current_operation = Operation.ADD
		

	def caller(self, type, id):

		if type == Type.NUMBER:
			print("num")
			self.number_call(id)
		elif type == Type.OPERATION:
			print("oper")
			self.operation_call(id)
		else:
			print("func")
			return self.functionality_call(id)

		print(id)
		print("Building :", self.building_number)
		print("Operation :", self.current_operation)

	def number_call(self, id):
		self.building_number += str(id)

	def operation_call(self, id):
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

		self.current_operation = Operation(id)
	
	def functionality_call(self, id):
		self.operation_call(1)
		result = self.result
		self.reset()
		return result

	def wrapper(self):
		self.current_number = float(self.building_number)
		self.building_number = ""

	def reset(self):
		self.result = 0.0
		self.current_number = 0.0
		self.building_number = ""
		print("RESET")

		self.current_operation = Operation.ADD

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




































#from Enums.Functionality import Functionality
#from Enums.Operation import Operation
#from Enums.Type import Type
#from Misc.Signs import *

## The class where all the calculation magic happens.
## There are a few concepts that defines how this works.
## The way the calculation works is:
## - The user starts clicking the numeric buttons, which call events which then
## operate all the logic,
##	and the current number being inputted is stored in self.current_number.
## - When the user clicks an operation or the equals functionality button, the
## program wraps up the number,
##   adds to the calc_list the inputted operation, and then initializes a new
##   object for the self.building_number.#
#class Calculation:
#	""" Manages the object for the calculation """
#	def __init__(self):
		
#		self.calculation = list()
#		self.building_number = ""

#		# Switch variable used for dis/allowing the input of operations
#		self.only_number = True

#	def caller(self, type, id):
#		if type == Type.NUMBER:
#			print("num")
#			self.number_call(id)
#		elif type == Type.OPERATION:
#			print("oper")
#			self.operation_call(id)
#		else:
#			print("func")
#			self.functionality_call(id)

#	def number_call(self, id):
#		print(id)
#		self.building_number += str(id)
#		self.only_number = False

#	def operation_call(self, id):
#		if not self.only_number:
#			print(id)
#			self.wrapper()
#			self.calculation.append(Operation(id))
	
#	# Manages all the functionalities
#	def functionality_call(self, id):
#		# if (calc != [] || build != "")

#		if id == Functionality.EQUALS:
#			if (not self.calculation.count == 0 or not self.building_number == ""):
#				print("func called")
#				self.wrapper()
#				self.calculate(id)
#		elif id == Functionality.CLEAR:
#			self.clear()
#		elif id == Functionality.DELETE:
#			self.delete()

#	def calculate(self, num):
#		string = ""

#		if self.calculation.count == 1:
#			print("cu")
#			string += self.calculation[0]

#		for x in self.calculation:
#			if str(x)[0] == 'O':
#				string += operation_sign()[x]
#			else:
#				string += str(x)
#			string += " "

#		print(string)

#		self.calculation = list()
#		self.building_number = ""

#	def wrapper(self):
#		self.calculation.append(float(self.building_number))
#		self.building_number = ""
#		self.only_number = True

#	def clear(self):
#		self.building_number = ""
#		self.calculation = list()
#		self.only_number = True

#	def delete(self):
#		if (self.building_number.count >= 1):
#			self.building_number.a