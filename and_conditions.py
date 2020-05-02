### 16/04/2020
### Author: Omer Goder
### Checking multiple conditions with the and condition

username = input("Welcome, please enter your username.\n\n")
password = input("\n\nPlease enter your password\n\n")

if username != 'omer' and password != 'pass@123':
    print("Access denied.")
else:
    print("\n\nWelcome " + username.title())
    print("\n")


