### 05/05/2020
### Author: Omer Goder
### Keyword Arguments

def book_description(book_type, author):
	"""Display book info"""

	print("\nThis is a " + book_type.title() + " book.")
	print("The author is: " + author.title())

book_description(book_type = 'non-fiction', author = 'brad stone')