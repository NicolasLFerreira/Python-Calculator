from Core.Calculation.Calculation import Calculation

class CalculationComponent:
	""" Component of the calculation """
	def __init__(self, type, id):

		# EnumType which used to identifying the variable.
		self.type = type

		# Used to identify the item within the Type.
		self.id

		# The current holding data
		self.content = []

	def append_data(self, data):
		self.content.append(data)

	def set_data(self, data):
		self.content = [].append(data)

	def clear_data(self):
		self.content.clear()