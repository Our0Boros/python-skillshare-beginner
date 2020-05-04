### 18/04/2020
### Author: Omer Goder
### Using IF statements with lists

# Creating our shopping cart
shopping_cart = ['pens','paper','stapler','post-its']

# Adding each item to an order
for item in shopping_cart:
    if item == 'pens' or item == 'stapler':
        print("Sorry, " + item + " is out of stock")
    else:
        print("Adding " + item + " to your order")
    
if 'pens' in shopping_cart:
    if 'paper' in shopping_cart:
        print("Enjoy your office supplies ;-)")
print("\nYour order is complete")



### My own code

# Write a program that builds a list from the user and prints out at the end
# if the list is empty notify the user he must add in more items to continue
# after each item is added, the user should be notified that the item is successfully added
# if an item is missing (post-its, paper clips - will be missing), inform the user
# the shopping cart can only contain up to 10 items (including)

import sys

cart = []
count = 0
missing_items = ['1610 printer','paper clips']
char = 'y'
print("\n\nHello and welcome to online shopping.")

if not cart:
    print("Your cart is emtpy.")

char = input("Would you like to add items to your cart? (Y/N):  ").lower()
if char == 'n':
    print("\nYou have selected not to continue with the shopping proccess\nHave a nice day.")
    sys.exit()
else:

    while count < 10 and char != 'n':
        item = input("\nWhat would you like to add to the list ")
        if item not in missing_items:
            cart.append(item)
            print(item.title() + " was added to your list.")
            count += 1
        else:
            print("\nSorry, this item is not available.\n")

        if count == 10:
            print("\nYou have reached the maximum amount of items (10) in your cart\n")
        else:                
            char = input("\nIf you would like to add another item enter'Y/y'\nElse enter 'N/n': ").lower()

    print("\nHere is your shopping list: \n")
    for item in cart:
        print(item)
