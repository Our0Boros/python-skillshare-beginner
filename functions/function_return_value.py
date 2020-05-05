### 05/05/2020
### Author: Omer Goder
### Returning a value in a function

def formatted_name(first_name, last_name):
	"""Return a formatted name"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

name = formatted_name('omer','goder')
print(name)

def formatted_username(email_address):
	"""Return a formatted username"""
	username = email_address.strip()
	return username
user = formatted_username('omer@googler.glass.org  ')
print(user)