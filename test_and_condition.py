### 16/04/2020
### Author: Omer Goder
### Asking and verifying username and password

cond = True
while cond == True:
    username = input("Please choose a username.\n\n")
    pass_1 = input("Choose password.\n\n")
    pass_2 = input("Confirm password\n\n")

    if pass_1 == pass_2:
        print("\nUsername and password has been successfully set\n\nWelcome to the system")
        cond = False
    else:
        print("Passwords do not match\n\nTry again")

print("You are now welcome to access the system\n\n")



while 1:

    Username = input("Enter username.\n")
    Password = input("Enter your password.\n")

    if Username == username and Password == pass_1:
        break
    else:
        print("\nAccess denied!\nTry again\n")
        
print("\nAccess granted\nEnjoy\n")

