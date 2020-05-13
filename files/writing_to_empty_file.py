### 13/05/2020
### Author: Omer Goder
### Writing to an empty file

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("Hello Everyone\n")

with open(filename, 'a') as file_object:
	file_object.write("And Welcome")