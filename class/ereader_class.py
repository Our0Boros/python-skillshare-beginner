### 08/05/2020
### Author: Omer Goder
### Creating a new reader class

class Ereader():
	"""A class to represent an ereader"""

	def __init__(self, make, model, backlight, battery, screen_type):
		"""Initialize the attributes to describe an ereader"""
		self.make = make
		self.model = model
		self.backlight = backlight
		self.battery = battery
		self.screen_type = screen_type
		self.library_count = 0 # Setting a default value

	def get_ereader_name(self):
		"""Return a formatted descriptive name for our ereader"""
		long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
		return long_name.title()

	def read_library_count(self):
		"""Show the amount of ebooks in our kindle library"""
		print("You have %d books in your kindle library" % (self.library_count))

my_new_ereader = Ereader('amazon kindle', 'paperwhite', 'adjustable', 'several monthes of barrty life', '300 dpi')
print(my_new_ereader.get_ereader_name())

# Modifying an attribute value directly
my_new_ereader.library_count = 36 
my_new_ereader.read_library_count()
