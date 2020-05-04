### 04/05/02020
### Author: Omer Goder
### Removing values from a list

books = ['big data', 'checklists', 'the firm', 'tesla', 'the firm', 'the firm']
count = 0

while 'the firm' in books:
	books.remove('the firm')
	count += 1

if count == 0:
	for book in books:
		print (book.title())
elif count >= 0:
	print("Those are the books in the list: ")
	for book in books:
		print (book.title())
	print("The book: 'The Firm' has been removed from the list "
		+ str(count) + " times\n")