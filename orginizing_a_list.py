### 14/04/2020
### Author: Omer Goder
### Orginizing a list

#creating a list of monthes
birthday_months = ['may','november','june']

birthday_months.sort() # Sorts alphabetically
print("The list - sort")
print(birthday_months)

# Using the reverse sort method
birthday_months = ['may','november','june']

birthday_months.sort(reverse=True) # Reverse alphabetical order
print("\nthe list - sort reverse")
print(birthday_months)

# By using the sort and the sort(reverse=True)
# The list is perminatelly altered, and can't go back to the original format

# We can use the sorted() method in order to temporerally sort a list


birthday_months = ['may','november','june']
print("\nthe list - sorted")
print(sorted(birthday_months))

print("\nthe list - original")
print(birthday_months)

# Reverse a list

birthday_days = ['monday','tuesday','wednesday','thursday','friday']
print("\nnew list - original")
print(birthday_days)

birthday_days.reverse()
print("\nnew list - reverse")
print(birthday_days)
print("\n")