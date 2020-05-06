### 06/05/2020
### Author: Omer Goder
### Modifying a list in a function

# Airline booking

# Write a function that passes a passenger 
# from a non-checked-in to a checked-in list
# the function arguments are the two lists and the passenger name

def check_in(non_checked_in, checked_in, passenger):
	for name in non_checked_in:
		if name == passenger:
			idx = non_checked_in.index(name)
			checked_in.append(non_checked_in[idx])
			non_checked_in.remove(name)

def move_all(non_checked_in, checked_in):
	while non_checked_in:
		checked_in.append(non_checked_in.pop())



non_checked_in = ['amram','annis', 'moai']
checked_in = ['ipkis','stas','mark','maor']
passed = check_in(non_checked_in, checked_in,'moai')

print("Checked in: ")
for passenger in checked_in:
	print(passenger.title())

print("\nNot checked in: ")
for passenger in non_checked_in:
	print(passenger.title())



move_all(non_checked_in,checked_in)
print("\nAfter everyone is checked in: ")
for passenger in checked_in:
	print(passenger.title())


