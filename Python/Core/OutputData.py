class OutputData():
	"""Class for holding the necessary data for the input in a way that's easily organizable"""
	def __init__(self, is_number = True, first = True, rad_operation = False, current_operation = None, building_number = [], result = 0.0, error = "ERROR: 00"):
		self.is_number = is_number
		self.first = first
		self.rad_operation = rad_operation
		self.current_operation = current_operation
		self.building_number = building_number
		self.result = result
		self.error = error