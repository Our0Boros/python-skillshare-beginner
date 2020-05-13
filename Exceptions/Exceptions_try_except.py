### 13/05/2020
### Author: Omer Goder
### Using the try-except block

try:
	print(0/0)
except ZeroDivisionError: # Only accept ZeroDivisionError
	print("You cannot divide by zero")

try:
	print(5/0)
except:
	print('There is some error')
