### 15/05/2020
### Author: Omer Goder
### Working with json.dump() function

import json

phone_numbers = ['202-555-0159', '202-555-0156','202-555-0158']


with open('phone_numbers.json', 'w') as file_object:
	json.dump(phone_numbers, file_object)
	# for phone_number in phone_numbers:
	# 	json.dump(phone_number, file_object)


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
with open('data_file.json','w') as file_object:
	json.dump(data, file_object, indent = 4, separators = ("."," = "))
