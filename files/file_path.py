### 13/05/2020
### Author: Omer Goder
### Read a file through a path

file_path = 'C:/Users/owner/Documents/GitHub/python-skillshare-beginner/My guide/Python Commands and Methods.txt'

with open(file_path) as object_file:
	content = object_file.read()
	print(content.strip())