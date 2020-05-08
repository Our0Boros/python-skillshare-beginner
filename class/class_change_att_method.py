### 08/05/2020
### Author: Omer Goder
### Modifying an attribute value through a method

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
	# Modifying an attribute value through a method
	def add_library_count(self, ebooks_added):
		"""adds or decrease the amount of ebooks on your library"""
		if ebooks_added < 0:
			print("You already have no ebooks\n")
		else:
			print("\n%d new ebooks has been added to your library" % (ebooks_added))
			self.library_count += ebooks_added


my_new_ereader = Ereader('amazon kindle', 'paperwhite', 'adjustable', 'several monthes of barrty life', '300 dpi')
print(my_new_ereader.get_ereader_name())

my_new_ereader.add_library_count(6)
my_new_ereader.read_library_count()
