### 13/05/2020
### Author: Omer Goder
### Making a list from a file

file_path = 'C:/Users/owner/Documents/GitHub/python-skillshare-beginner/My guide/Python Commands and Methods.txt'

with open(file_path) as object_file:
	lines = object_file.readlines()

for line in lines:
	print(line)