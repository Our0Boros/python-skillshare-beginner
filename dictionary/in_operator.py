### 21/04/2020
###Author: Omer Goder
### Using a key to get a value

# Create a dictionary of terms
terms = {'variable' : 'represents or refers to a value stored in memory' , 'string' : 'A sequence of characters'}

if 'float' in terms:
	print("I know a float is.")
else:
	print("I don't know what that is.")

print(terms['variable'] + " " + terms['string'] + "\n")

# Creating an empty dictionary
terms = {}

# Adding new values to a dictionary
terms['variable'] = 'represents or refers to a value stored in memory.'
terms['integer'] = 'A whole number.'

print(terms['variable'])
print(terms['integer'])
