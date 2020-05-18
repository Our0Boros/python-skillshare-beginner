### 18/05/2020
### Author: Omer Goder
### Storing and reading user data

import json

filename = 'username.json'

try:
	with open(filename) as f1:
		username = json.load(f1)
except FileNotFoundError:
	username = input("What's your saint nick's name")
	with open(filename, 'w') as f2:
		json.dump(username, f2)
else:
	print("Welcome back %s!" % username)

