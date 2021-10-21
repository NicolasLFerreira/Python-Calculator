class OutputData():
	"""Class for holding the necessary data for the input in a way that's easily organizable"""
	def __init__(self, is_number = True, first = True, current_operation = None, building_number = [], result = 0.0, error = "Unknown error"):
		self.is_number = is_number
		self.first = first
		self.current_operation = current_operation
		self.building_number = building_number
		self.result = result
		self.error = error