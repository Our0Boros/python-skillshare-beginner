## Exceptions

- There are cases of which we will get an error from the parser
- It is possible to use Exceptions to test cases that returns an error<br>
and decide what to do instead
- When an exception is raised, we can print a costume message or perform a series of actions

#### try-except block
- The try-except block allows us to "try" a case and if there is an error, print a message or perform actions

##### example:
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
