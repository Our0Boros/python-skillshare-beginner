### 14/05/2020
### Author: Omer Goder
### FileNotFoundError

filename = 'somename.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	print('Sorry, the file \'' + filename + '\' could not be found.')


	