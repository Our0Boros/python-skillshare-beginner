### 06/05/2020
### Author: Omer Goder
### Using a while loop in a function

def get_formatted_name(first_name, last_name):
    """return a full name formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print('\nWhat is your name?')
    first_name = input('First name: ')
    if first_name == 'q':
        break
    last_name = input('Last name: ')
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)

    print('\nHello, ' + formatted_name + '!')
