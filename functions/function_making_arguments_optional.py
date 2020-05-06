### 05/05/2020
### Author: Omer Goder
### Making arguments optional

def formatted_name(first_name, last_name , middle_name = ''):
	"""Return a full name"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

name = formatted_name('goder','jakobi','dadush')
print(name)

name = formatted_name('goder','dadush')
print(name)