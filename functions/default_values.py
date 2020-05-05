### 05/05/2020
### Author: Omer Goder
### Defauly Values

def book_description(author, book_type = 'non-fiction'):
	"""display book info"""
	print("\nThis book is a %s. " % book_type.title())
	print("The author of this book is: " + author.title())

# Using the default value
book_description('ashlee vance')
# Replacing the default value
book_description('j.k rowling', 'fiction')