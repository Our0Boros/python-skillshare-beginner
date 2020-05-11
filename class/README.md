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
				
	def __init__(self, att_1, att_2, ...):
		"""Initialize all attributes"""
		self.att_1 = att_1
		self.att_2 = att_2
		self...
				
	def method_1(self, args):
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
- **Note:** The `__init__()` method is called automatically every time the class is being used to create a new object.
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
- By default the child (derived) inherits the aruments and methods from the parent (base)
- syntex: `class Child_class(Parent_class):
<br>

##### the `__init__` method in a child class
- The `__init__` method in a derived (child) class, by it self<br>
clears the arguments from the parent (base) class
- **Note:** The child's `__init__()` method overrides the inheritance of the parent's `__init__()` method.
<br><br>
- To keep the inheritance of the parent's`__init__()` method, add a call to the parent's `__init__()` method:

##### example:
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```

#### the super() Function
- Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

##### example:
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```

#### Override methods
- Python enables a child class to override a method from the parent class
- This can be done by naming the method in the child class in the exact same name<br>
as the method we would like to replace in the parent class

##### example:
```
class Ereader(): # Parent class
	"""A class to represent an ereader"""

	def __init__(self, make, model, backlight, battery, screen_type):
		"""Initialize the attributes to describe an ereader"""
		self.make = make
		self.model = model
		self.backlight = backlight
		self.battery = battery
		self.screen_type = screen_type
		self.library_count = 0 # Setting a default value
	
	def describe_backlight(self):
		"""Descibe the backlight of our ereader"""
		print("The back light of this ereader allows you to read in the dark")		
		
class KindleFire(Ereader): # Child class
	"""Represents aspects of an ereader specific to a kindle fire
	Then itialize attributes specific to a kidnle fire"""

	def __init__(self, make, model, backlight, battery, screen_type, screen_resolution = '1280 * 800 px'):
		"""initialize attributes for the kindle fire"""
		self.screen_resolution = screen_resolution

		super().__init__(make, model, backlight, battery, screen_type)

	def describe_backlight(self): # This will override the same method name in the parent class
		"""The kindle fire does not have a backlight"""
		print('The color screen lets you read in the dark')

```


#### Using a class as an attribute
- There will be cases where we will have to many atrributes for a class<br>
In those cases we could use another class to hold the attributes for the main class

for example: a tablet will have several multiple attributes such as size, color, battery, screen type<br>
but screen type will also have different attributes such as glass grade, color/bw, screen size, ...

##### example:
```
class Tablet():
	"""This will be the class that uses the attribute."""

	def __init__(self, thickness, color, battery):
		"""Initialize a parameter as a class"""
		self.thickness = thickness
		self.color = color
		self.battery = battery
		self.screen = Screen()


class Screen():
	"""This will be the attribute for the other class."""

	def __init__(self, glass_grade = 'gorilla glass', color = 'BW', screen_size = '8"'):
		"""Initalize the attributes of the Attrib class."""
		self.glass = glass_grade
		self.color = color
		self.screen_size = screen_size


	def screen_type(self):
		"""Print the attributes"""
		print("Glass: " + self.glass + "\nSize: " + self.screen_size + ".")

	def screen_color(self):
		"""Print the arguments."""
		print("This is a " + self.color + " screen.\n")


my_tablet = Tablet('5 mm', 'green', '4800 mAh')
my_tablet.screen.screen_type()
my_tablet.screen.screen_color()

my_screen = Screen('Gorilla 8', 'color', '10"')
my_tablet.screen = my_screen
my_tablet.screen.screen_type()
my_tablet.screen.screen_color()
```

Output:
```
Glass: gorilla glass
Size: 8".
This is a BW screen.

Glass: Gorilla 8
Size: 10".
This is a color screen.
```

#### Import class
- After we're done writing and checking that our class is working correctly,<br>
	we can save is as a module to be used by other programs
* syntex: from module_name import class_name

##### example:
```
from ereader_class import Ereader

my_ereader = Ereader('amazon', 'kindle fire', 'backlight', '12 hour battery life', 'color screen')
my_ereader.read_library_count()
```
