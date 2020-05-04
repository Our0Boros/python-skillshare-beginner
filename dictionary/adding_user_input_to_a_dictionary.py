### 04/05/2020
### Author: Omer Goder
### Adding user input to a dictionary

# Creat an empty dictionary
rental_properties = {}

# Set a flag to indicate we are taking apllications
rental_open = True

while rental_open: # while True
	# prompt users for name and address.
	username = input("\nWhat is your name?")
	rental_property = input("What is the address of the property you would like to rent?")

	# Store the responses in a dictionary
	rental_properties[username] = rental_property

	# Ask if the user knows anyone else who would like to rent their property
	repeat = input("\nDo you know anyone how might like to rent out their propery?\t(Y/N)").lower()
	if repeat == 'y':
		continue # just to check code upgrading option
	else:
		rental_open = False

# Adding propery is complete
print('\n---Property to rent---')
for username, rental_property in rental_properties.items():
	print(username.title() + " have a property at " + rental_property.title() + " to rent.")
