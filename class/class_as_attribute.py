### 10/05/2020
### Author: Omer Goder
### Using a class as an attribute to another class


class Main():
	"""This will be the class that uses the attribute."""

	def __init__(self):
		"""Initialize a parameter as a class"""
		self.attrib_1 = Attrib()
		
class Attrib():
	"""This will be the attribute for the other class."""

	def __init__(self, att = 'attribute'):
		"""Initalize the attributes of the Attrib class."""
		self.arg_1 = att

	def print_att(self):
		"""Print the attributes"""
		print("These are the attributes: ...")

	def print_args(self):
		"""Print the arguments."""
		print("These are the arguments: ...")

instance = Main()
instance.attrib_1.print_att()
instance.attrib_1.print_args()