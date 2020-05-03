### 16/04/2020
### Author: Omer Goder
### Python's if statement

print("To continue please log in.")
i = 0
count = 0
#using the if statement
while i == 0:
    
    password = input("Please enter your password.")
    if password == "pass@123":
        print("Access granted")
        i=1
        print("Welcome to the system")
        break
    else:
        count = count + 1
        if count == 10:
            print("Too many attemps\nPlease restart the program\n")
            break
        print("Please try again")
    
