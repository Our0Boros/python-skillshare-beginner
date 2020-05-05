### 05/05/2020
### Author: Omer Goder
### Positional arguments


def book_description(book_type, author_name):
	"""Display book information"""
	print("\nThis book is a " + book_type.title() + ".")
	print("The author of this book is: " + author_name.title() + ".")

# Using a default argument
def name_age(name, age = 35):
	print("\n%s is %d years old" %(name.title(), age))

book_description('non-fiction', 'ashlee vance')
book_description('fiction', 'dan brown')

book_type = 'pyshics'
author_name = 'james'
book_description(author_name, book_type)

name = 'mike'
age = 50
name_age(name, age)