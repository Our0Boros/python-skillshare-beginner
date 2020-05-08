### 08/05/2020
### Author: Omer Goder
### Inheritance

"""
-	A parent class must be in the same file as the child class
-	The child class must be written after the parent class
"""

class Ereader(): # Parent class
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
	
	def update_library_count(self, ebooks_number):
		"""Set the amount of ebooks in the library"""
		self.library_count = ebooks_number

	def reset_library_count(self):
		self.library_count = 0


class KindleFire(Ereader): # Child class
	"""Represents aspects of an ereader specific to a kindle fire
	Then itialize attributes specific to a kidnle fire"""

	def __init__(self, make, model, backlight, battery, screen_type):
		"""initialize attributes for the kindle fire"""
		super().__init__(make, model, backlight, battery, screen_type)

my_kindle_fire = KindleFire('amazon', 'kidle fire', 'backlight', '12 hour battery life', 'color screen')
print(my_kindle_fire.get_ereader_name())

