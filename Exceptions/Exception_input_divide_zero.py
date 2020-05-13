### 13/05/2020
### Author: Omer Goder
### Zero Division Error

print("Enter q to quit")
while True:
    num1 = input("Enter first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter second number: ")
    if num2 == 'q':
        break
    try:
        answer = int(num1) / int(num2)
    except ZeroDivisionError:
        print("You can't divide by zero!!!")
    else:
        print("Answer = " + str(answer))
