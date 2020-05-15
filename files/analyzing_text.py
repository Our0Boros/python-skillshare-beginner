### 14/05/2020
### Author: Omer Goder
### Analyzing Text

file_path = 'C:/Users/owner/Documents/GitHub/python-skillshare-beginner/My guide/'
filename = 'Python Commands and Methods.txt'

try:
	with open(file_path + filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	print("Sorry, the file '" + filename + "' cannot be found.")
else:
	words = contents.split()
	number_words = len(words)
	print("The file '" + filename + "' has aprroximatly " + str(number_words) + " words in it")

	print(type(words))