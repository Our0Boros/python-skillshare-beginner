### 01/05/2020
### Author: Omer Goder
### Nesting a list inside a dictionary

# Creating a dictionary with a nested list
car = {
	'model' : 'standard',
	'extra features' : ['cup holder', 'heated seats', 'wheel cover']
}

#print out the car model

print("You ordered the " + car['model'].title() + " model\nWith the following extra features:")

for extra in car['extra features']:
	print (extra.title())
