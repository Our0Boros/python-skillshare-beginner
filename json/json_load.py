### 15/05/2020
### Author: Omer Goder
### Working with json.load() function

import json

filename = 'phone_numbers.json'


with open(filename) as f:
	data = json.load(f)
print(data)