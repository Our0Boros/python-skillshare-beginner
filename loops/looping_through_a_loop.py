### 15/04/2020
### Author: Omer Goder
### Looping through a list

months = ['january','fabruary','march','april','may','june','july','august','september','october','november','december']

# Using a for loop to print a list
for month in  months:
	print("The next month is:\t" + month)
	print('\n')
print("\nEnd of program\n") # Print out once - not in the loop


#example for indexing using enumeration (considers non-pythonic)
#for index, month in enumerate(months):
	# print(index, month.title() + " is a name of a month\n")
