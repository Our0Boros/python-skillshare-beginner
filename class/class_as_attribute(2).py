### 11/05/2020
### Author: Omer Goder
### Using a class as an attribute to another class


class Tablet():
	"""This will be the class that uses the attribute."""

	def __init__(self, thickness, color, battery):
		"""Initialize a parameter as a class"""
		self.thickness = thickness
		self.color = color
		self.battery = battery
		self.screen = Screen()


class Screen():
	"""This will be the attribute for the other class."""

	def __init__(self, glass_grade = 'gorilla glass', color = 'BW', screen_size = '8"'):
		"""Initalize the attributes of the Attrib class."""
		self.glass = glass_grade
		self.color = color
		self.screen_size = screen_size


	def screen_type(self):
		"""Print the attributes"""
		print("Glass: " + self.glass + "\nSize: " + self.screen_size + ".")

	def screen_color(self):
		"""Print the arguments."""
		print("This is a " + self.color + " screen.\n")


my_tablet = Tablet('5 mm', 'green', '4800 mAh')
my_tablet.screen.screen_type()
my_tablet.screen.screen_color()

my_screen = Screen('Gorilla 8', 'color', '10"')
my_tablet.screen = my_screen
my_tablet.screen.screen_type()
my_tablet.screen.screen_color()