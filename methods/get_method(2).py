### 21/04/2020
### Author: Omer Goder
### Editing & deleting values in a dictionary

# terms = {'integer' : 'Is a number that contains a decimal place.'}

# terms['integer'] = 'A whole number'

# print(terms.get('integer'))

terms = {'integer' : 'Is a number that contains a decimal place.' , 'string' : 'a sequence of characters.'}

del terms['integer']

print(terms)
