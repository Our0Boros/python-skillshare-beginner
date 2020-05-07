### 07/05/2020
### Author: Omer Goder
### Pulling book information

# Creating a list of books (list of dicionaries)

from book_functions import books_available, author_info

book_1 = {'name' : 'winds of change', 'author' : 'peter hannessy', 'publisher' : 'penguin books'}
book_2 = {'name' : 'introduction to multimodal analisys', 'author' : 'per ledin', 'publisher' : 'blumsbury'}
books = [book_1, book_2]

# Creating a dictionary of authors books (dictionary of lists)
authors = {'peter hannessy' : ['winds of change', 
'the prime minister', 'having it so good', 
'white hall', 'the cabinet'],
'per ledin' : ['introduction to multimodal analisys',
'Doing Visual Analysis: From Theory to Practice']}


author = books_available(books, 'winds of change')
print("\n")
author_info(author, authors)
