### 06/05/2020
### Author: Omer Goder
### Arbitrary arguments

def creat_passenger(*requests):
	"""print user requests"""
	print("Passenger requests: ")
	for request in requests:
		print("-" + request)

creat_passenger('window seat', 'seat near the top of the plane', 'pre-order meal')