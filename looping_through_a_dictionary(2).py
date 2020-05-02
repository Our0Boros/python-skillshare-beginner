### 24/04/2020
### Author: Omer Goder
### Other ways to loop through a dictionary

birthday_months = {
	'tony' : 'november',
	'pat' : 'june',
	'mary' : 'may',
}
for name in birthday_months.keys():
	print(name.title())

for month in birthday_months.values():
	print(month)

print(birthday_months.keys())

this_set = {"apple" , 'apple' , "cherry"}
print(this_set)