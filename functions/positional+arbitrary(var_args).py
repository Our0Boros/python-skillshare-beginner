### 06/05/2020
### Author: Omer Goder
### Using positional and arbitrary arguments together

def assign_seat(seat, *requests):
	"""Assign a seat and requests to a passenger"""
	print("\nThe passenger in seat %d has made the follwing requests:" % (seat))
	for request in requests:
		print("- " + request)

assign_seat(5, 'window seat', 'pre-order breakfast', 'extra leg space')