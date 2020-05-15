### 14/05/2020
### Author: Omer Goder
### Working with multiple files


def word_count(filename):
	"""Count the number of words in a file"""

	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("Sorry, the file '" + filename + "' cannot be found.")
	else:
		words = contents.split()
		number_words = len(words)
		print("The file '" + filename + "' has aprroximatly " + str(number_words) + " words in it")

filenames = ['arbitrary_keyword_arguments.py', 'class_change_att_method.py']

for filename in filenames:
	word_count(filename)