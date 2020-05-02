### 13/04/2020
###Author: Omer Goder
### how to edit lists


# Creating a list of monthes
brithday_months = ['spril','may','november']

# Print our list
print(brithday_months)

# Changing an element of the list
brithday_months[0] = 'april' 

print(brithday_months)

# Using the append method
brithday_months.append('june')

print(brithday_months)

# Creat an empty list / Empty the list
brithday_months = []

print(brithday_months)

brithday_months.append('august') # Add a new item to the end of the empty list

print(brithday_months)

# Using the insert method - .insert(pos,'str')
brithday_months.insert(0,'may')

print(brithday_months)

# Using the delete statement
del brithday_months[1] 

print(brithday_months)