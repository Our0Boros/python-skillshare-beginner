### 13/05/2020
### Author: Omer Goder
### Reading a file line by line

file_path = 'C:/Users/owner/Documents/GitHub/python-skillshare-beginner/My guide/'
file_name = 'Python Commands and Methods.txt'

with open(file_path+file_name) as object_file:
	for line in object_file:
		print(line.strip())