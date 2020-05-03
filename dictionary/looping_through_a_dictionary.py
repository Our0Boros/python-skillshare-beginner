### 24/04/2020
### Author: Omer Goder
### Looping through a dictionary

birthday_months = {
	'tony' : 'november',
	'pat' : 'june',
	'mary' : 'may',
}

for key, value in birthday_months.items():
	print("\nName: " + key)
	print("Month: " + value)
	print(key.title() + 'was born in: ',end='')
	print(value)
print("\nBirthday Months: ")
print(birthday_months.items())


# Looping through key-value pairs
book_1 = {
	'name' : 'elon musk',
	'author' : 'ashlee vance',
	'price' : '14.99',
	'publisher' : 'virgin books',
}

for key, value in book_1.items():
	print("\nKey: " + key.title())
	print("Value: " + value.title())

print("\n\n")
for key, value in book_1.items():
	print("\n" + key.title() + "\t:\t" + value.title())

items = book_1.items()
print("\n\n")
del book_1['name']
print(items)
