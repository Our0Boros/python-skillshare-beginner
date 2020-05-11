### 07/05/2020
### Author: Omer Goder
### Creating first class

class  Book(): #Capitalize names refer to a class in python
	"""A class to creat a book."""

	def __init__(self, name, price, publisher):
		"""Initialize the name, price, and publisher."""
		self.name = name
		self.price = price
		self.publisher = publisher

	def hardback(self):
		"""Simulate a hardback book."""
		print(self.name.title() + " is a hardback book.\n")

	def softback(self):
		"""Simulate a softback book."""
		print(self.name.title() + " is a softback book.\n")

	def ebook(self):
		"""Simulate an ebook"""
		print(self.name.title() + " is an ebook.\n")

	def ebook_reader(self):
		"""Simulate an ebook reader"""
		print("\nLibrary: " + self.name.title() + "\nPrice: $" + str(self.price) + "\nPublisher: " + self.publisher + ".\n")

# # Creat an instance of our Book class
# my_book = Book('elon musk', 14.99, 'virgin books')
# your_book = Book('the everything store', 9.99, 'virgin books')

# # Accessing attributes
# print("I'm currently reading " + my_book.name.title() + ".")
# print("This books cost: $%.2f." % my_book.price)

# # Calling our ebook_reader method
# my_book.ebook_reader()
# your_book.hardback()
