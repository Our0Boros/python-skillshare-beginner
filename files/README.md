## Files 

#### Open function
- In order to do any work with a file we first need to open it to access it
- The open function need just one argument (the file name) to open it
- The open fiunction returns an object representing the file (file_object)
- Python looks for the file in the same directory it's being stored
  - so we need to make sure that all our programs and text files are in the same directory

#### with keyword
- The python keyword with in front of the open function closes the file once access to it is no longer required

#### read method
- This method reads the entire content of the file and stores it as one long string

##### example:
```
with open('Python Commands and Methods.txt') as object_file:
	content = object_file.read()
	print(content.strip())
```
#### File path
- If the file we would like to work with is not in the same directory as the program we can use the file path
- The file path tells the program where to find the file

##### example:
```
file_path = 'C:/Users/owner/Documents/GitHub/python-skillshare-beginner/My guide/Python Commands and Methods.txt'

with open(file_path) as object_file:
```
#### Read line by line
- We can use a for loop to run through the file line by line

##### example:
```

with open(file_path+file_name) as object_file:
	for line in object_file:
		print(line.strip())
```

#### Creat a list from a file (.readlines() function)
- The `readlines()` function in Python takes a text file as input <br>
and stores each line in the file as a separate element in a list.

##### example:
```
with open(file_path) as object_file:
	lines = object_file.readlines()

for line in lines:
	print(line)
```

#### Create a New File
- To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

##### example 1:
```
filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("Hello Everyone\n")

with open(filename, 'a') as file_object:
	file_object.write("And Welcome")
```

##### example 2:
```
filename = 'User Input.txt'

user_input = input('Enter new line to the file')

with open(filename, 'a') as file_object:
	file_object.write(user_input + "\n")
```
