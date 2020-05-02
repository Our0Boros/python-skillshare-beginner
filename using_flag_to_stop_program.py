### 01/05/2020
### Author: Omer Goder
### Using a flag to stop a program

prompt = '\nThis is a new line'
prompt += '\nThis line will keep on printing untill you enter \'q\'\t'

# Set flag to True
active = True
while active:
    message = input(prompt)

    if(message == 'q'):
        active = False
    else:
        print("\n")
        print(message)

