### 17/04/2020
### Author: Omer Goder
### Age checker

your_age = input("How old are you? ")
friends_age = input("How old is your friend? ")

if int(your_age) >= 18 and int(friends_age) >= 18:
    print("Congrats, you both can vote!")
elif int(your_age) >= 18 or int(friends_age) >= 18:
    print("Sorry, one of you is too young to vote.\nthe other one still can")
else:
    print("Sorry, you're both under age, try again next year!")
