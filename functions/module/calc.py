
### 06/05/2020
### Author: Omer Goder
### Creating a module for later import

def sum(num_1 = 0, num_2 = 0):
	"""sum of two entered numbers (default is 0 at both)"""
	print("The sum:\t%d + %d = %d" % (num_1, num_2, num_1 + num_2))
	return num_1 + num_2
def sub(num_1 = 0, num_2 = 0):
	"""sub of two entered numbers (default is 0 at both)"""
	print("The sub:\t%d - %d = %d" % (num_1, num_2, num_1 - num_2))
	return num_1 - num_2
def multi(num_1 = 0, num_2 = 0):
	"""multi of two entered numbers (default is 0 at both)"""
	print("The multi:\t%d * %d = %d" % (num_1, num_2, num_1 * num_2))
	return num_1 * num_2
def dev(num_1 = 0, num_2 = 0):
	"""dev of two entered numbers (default is 0 at both)"""
	print("The dev:\t%d / %d = %d" % (num_1, num_2, num_1 / num_2))
	return num_1 / num_2
def mod(num_1 = 0, num_2 = 0):
	"""modulu of two entered numbers (default is 0 at both)"""
	print("The mod:\t%d %% %d = %d" % (num_1, num_2, num_1 % num_2))
	return num_1 % num_2
def pow(num_1 = 0, num_2 = 0):
	"""power of two entered numbers (default is 0 at both)"""
	print("The pow:\t%d ^ %d = %d" % (num_1, num_2, num_1 ** num_2))
	return num_1 ** num_2
