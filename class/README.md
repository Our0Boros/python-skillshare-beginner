## Class
- Classes provide a means of bundling data and functionality together. 
- Creating a new class creates a new type of object, allowing new instances of that type to be made. 
- Each class instance can have attributes attached to it for maintaining its state. 
- Class instances can also have methods (defined by its class) for modifying its state.
- a class name must start with a capital letter
* syntex:	
```
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
```


##### example:
```
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
```

The output will be:
```
Library: Elon Musk
Price: $14.99
Publisher: virgin books.
```

#### The __init__ method
- `__init__` is one of the reserved methods in Python. 
- In object oriented programming, it is known as a constructor. 
- The `__init__` method can be called when an object is created from the class, <br>
and access is required to initialize the attributes of the class.
- syntex: `def __init__(self, arg_1, arg_2, ...):`

##### example:
```
def __init__(self, name, price, publisher):
		"""Initialize the name, price, and publisher."""
		self.name = name
		self.price = price
		self.publisher = publisher
```

#### Set deafault values
- We can set default values to arguments within the `__init__` method
- syntex: `self.arg_1 = 'default_val'`

#### Class - Modify Attributes
- We can change the class atrributes values after
* syntex (dot natation): instance.attribute = new_val
	
##### example:
```my_new_ereader.library_count = 36 # direct modification using dot notation```

- We can modify the class atrributes values in a method of the class

##### example:
```
def update_library_count(self, ebooks_number):
	"""Set the amount of ebooks in the library"""
	self.library_count = ebooks_number
```

#### Inheritance
- Inheritance allows us to define a class that inherits all the methods and properties from another class.
- Parent class is the class being inherited from, also called base class.
- Child class is the class that inherits from another class, also called derived class.
- Child class must come after the parent class

- the `__init__` method in a child class
