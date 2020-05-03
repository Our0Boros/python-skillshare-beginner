### 17/04/2020
### Author: Omer Goder
### Interest rate checker using if-elif-else
import sys
# Get user balance
balance = input("What is your bank balance?")

if int(balance) <= 0:
    ch = input("Would you like to make a deposit?\nType Y/N:  ").lower()
    if ch == 'y':
        balance = input("How much would you like to deposit: ")
    else:
        print("Have a nice day.")
        sys.exit()
        
if int(balance) <= 50:
    print("You do not qualify for interest.")
elif int(balance) < 100:
    print("Your interset rate is 1%.")
else:
    print("Your interest rate is 2%.")
    
