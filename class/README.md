### Class
-	Classes provide a means of bundling data and functionality together. 
-	Creating a new class creates a new type of object, allowing new instances of that type to be made. 
-	Each class instance can have attributes attached to it for maintaining its state. 
-	Class instances can also have methods (defined by its class) for modifying its state.
*	syntex:	
			class Class_name():
				"""docstring of the class"""
				
				def __init__(self, arg_1, arg_2, ...):
					"""Initialize all arguments"""
					self.arg_1 = arg_1
					self.arg_2 = arg_2
					self...
				
				def method_1(args):
					"""docstring for method_1"""
					method_actions
			
**	a class name must start with a capital letter

	example:
				class  Book(): #Capitalize names refer to a class in python
					"""A class to creat a book."""

					def __init__(self, name, price, publisher):
						"""Initialize the name, price, and publisher."""
						self.name = name
						self.price = price
						self.publisher = publisher

					def ebook(self):
						"""Simulate an ebook"""
						print(self.name.title() + " is an ebook.\n")

					def ebook_reader(self):
						"""Simulate an ebook reader"""
						print("\nLibrary: " + self.name.title() + "\nPrice: $" + str(self.price) + "\nPublisher: " + self.publisher + ".\n")

				# Creat an instance of our Book class
				my_book = Book('elon musk', 14.99, 'virgin books')
				
				# Calling our ebook_reader method
				my_book.ebook_reader()
	
	The output will be:
	
	Library: Elon Musk
	Price: $14.99
	Publisher: virgin books.
