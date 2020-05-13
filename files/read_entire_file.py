### 11/05/2020
### Author: Omer Goder
### Read a file

with open('Python Commands and Methods.txt') as object_file:
	content = object_file.read()
	print(content.strip())