###01/05/2020
### Author: Omer Goder
### Using a long prompt line in an input command

prompt_line = "This is a very long line that is asking the user for an input"

user_input = input(prompt_line + "\n")

print("The user input is: ", end = '')
print(user_input)
