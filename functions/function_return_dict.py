### 06/05/2020
### Author: Omer Goder
### Returning a dictionary

def build_book(name, author, publisher):
	"""Create a dicionary of book information"""
	book = {'name' : name, 'author' : author, 'publisher' : publisher}
	return book

my_book = build_book('elon musk', 'ashlee vance', 'virgin books')

for key, value in my_book.items():
	print(key.title() + ": " + value.title())