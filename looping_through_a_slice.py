### 15/04/2020
### Author: Omer Goder
### Looping through a slice

# Looping through a slice with a for loop

names = ['tony','frank','mary','carl']
print("Here are the names of the last 3 registrations.")

for name in names[-3:]:
	print(name.title())