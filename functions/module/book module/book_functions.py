### 07/05/2020
### Author: Omer Goder
### Module for imoprt

def books_available(books, name):
	book_found = 0
	for book in books:
		if book['name'] == name:
			for key, value in book.items():
				print(key.title() + " : " + value.title())
				if key == 'author':
					author = value
			book_found = 1
	if book_found == 0:
		print("This book in not in the list")
	return author

def author_info(author_name, authors_list):
	if author_name in authors_list:
		print(author_name.title() + " published the following:")
		for key, value in authors_list.items():
			if key == author_name:
				for book in value:
					print('-' + book)


