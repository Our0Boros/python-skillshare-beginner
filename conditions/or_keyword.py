### 17/04/2020
### Author: Omer Goder
### Using the OR keyword to check values in a list

# Names registered
registered_names = ['tony','frank','mary','peter']

username = input("Please enter username you would like to use.\n\n").lower()

#Check to see if username is already taken
if username in registered_names:
    print("Sorry, username is already taken.")
else:
    print("This username is available")
