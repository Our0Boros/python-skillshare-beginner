### 25/04/2020
### Author: Omer Goder
### Using a dictionary in a list

book_0 = {'name' : 'elon musk' , 'author' : 'ashlee vance' , 'price' : '14.99' , 'publisher' : 'virgin books'}
book_1 = {'name' : 'team of rivals' , 'author' : 'doris kearns goodwin' ,'price' : '10.99', 'publisher' : 'simon & schuster'}
book_2 = {'name' : 'the everything store' , 'author' : 'brad stone','price' : '12.22', 'publisher' : 'little, brown and company'}

books = [book_0, book_1, book_2]

for book in books:
	print(book)
print('\n')

for book in books:
	for key in book.keys():
		print(key.title() + ": ", end='')
		print(book[key].title())

	print("\n")