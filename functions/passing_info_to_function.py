### 05/05/2020
### Author: Omer Goder
### Passing information to function

def welcome(username):
	"""Showing a username"""
	print("Hi " + username.title() + ".\n")

# Notice that the name of the argument sent to the function (call)
# doesn't have to be the same as the argument the function accepts
name = 'omer'
welcome(name)

# While using keyword arguments like the following
# the argument sent to the function (call)
# must be sent after the same name the function accepts
welcome(username = 'david')