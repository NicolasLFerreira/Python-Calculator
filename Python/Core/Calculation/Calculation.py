
# The class where all the calculation magic happens.
# There are a few concepts that defines how this works. 
# The way the calculation works is:
# - The user starts clicking the numeric buttons, which call events which then operate all the logic,
#	and the current number being inputted is stored in self.current_number.
# - When the user clicks an operation or the equals functionality button, the program wraps up the number,
#   adds to the calc_list the inputted operation, and then initializes a new object for the self.current_number.#

class Calculation:
	""" Manages the object for the calculation """
	def ____init__(self):
	
		# The data from the calculation will be held inside the self.calc_list object.
		self.calc_list = []

		# The current number being inputted by the user
		self.current_number

		# The last operation inputted by the user. Default is ADDITION because ''
		self.last_operation