### 24/04/2020
### Author: Omer Goder
### Learning how to work with sets in python

# Creating a set
# the add method
# the update method
# the len method
# the remove method
# the discard method
# the clear method
# the union method
# using the update method to combine two sets
# the set constructor command

# Creating a set
set_1 = {'apple','banana','cherry','apple'}
print(set_1)

# Using the add() method
set_1.add("orange")
print(set_1)

# Using the update method
set_1.update(['orange','mango','grapes'])
print(set_1)

# Using the len() method - length of set
set_len = len(set_1)
set_name = 'set_1'
print("There are %d items in the set: %s" % (set_len,set_name))
# str_len is an integer, needed to be converted to string 
# in order to be printed next to another string

# Using the remove method
set_1.remove('apple')
print(set_1)
# the remove method will raise an error 
# if the item is not in a set

# Using the discard method
set_1.discard('kiwi') # Not in the set
print(set_1)

# Using the clear method to clear a set
set_1.clear()
print(set_1)

# Deleting a set
del set_1
# If we tried printing set_1 we will get an error, because it's gone

set1 = {'a','b','c'}
set2 = {1,2,3}

set3 = set1.union(set2)
print('Set3: ')
print(set3)	

set1.update(set2)
print(set1)

# Using the set constructor command
set_platforms_1 = set(('apple','microsoft','google'))
print(set_platforms_1)
list_furits = ['apple','banana','cherry']
set_fruits = set(list_furits)
print(set_fruits)
