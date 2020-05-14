## Exceptions

- There are cases of which we will get an error from the parser
- It is possible to use Exceptions to test cases that returns an error<br>
and decide what to do instead
- When an exception is raised, we can print a costume message or perform a series of actions

#### try-except block
- The try-except block allows us to "try" a case and if there is an error, print a message or perform actions
- syntex:
```
try:
	(test object)
except Trackback_Error_Name: # Trackback_Error_Name is all errors by default, check examples below
	(what to to if an error is raised)
else: #optional
	(what to do if an error is not raised)
```

##### example 1:
```
try:
	print(0/0)
except ZeroDivisionError: # Only accept ZeroDivisionError
	print("You cannot divide by zero")

try:
	print(5/0)
except: # Accept any error
	print('There is some error')
```
##### example 2:
```
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
```
