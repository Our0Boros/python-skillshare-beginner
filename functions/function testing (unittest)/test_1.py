### Testing Exceptions
from math import pi
import unittest
def circle_area(r):
	"""Calculate the area of a circle"""
	if r > 0:
		A = pi*r**2
		return A
	else:
		print("R must be greater than zero!!!")

class CircleAreaTest(unittest.TestCase):
	"""Testing the area of a circle function"""
	def test_circle_area(self):
		self.assertEqual(circle_area(2), pi*2**2)

unittest.main()



