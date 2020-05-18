## JSON files

- JSON is a syntax for storing and exchanging data
- JSON is text, written with JavaScript object notation
- JSON supports primitive types, like strings and numbers, as well as nested lists and objects
- JSON - **J**ava**S**cript **O**bject **N**otation<br>

#### Importing json
```python
import json
```

##### example of json file
```javascript
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

#### A Little Vocabulary
The process of encoding JSON is usually called **serialization**.<br>This term refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network.<br>Naturally, **deserialization** is the reciprocal process of decoding data that has been stored or delivered in the JSON standard.

#### Serializing JSON
What happens after a computer processes lots of information? It needs to take a data dump. <br>Accordingly, the json library exposes the dump() method for writing data to files. There is also a dumps() method (pronounced as “dump-s”) for writing to a Python string.
<br><br>
Simple Python objects are translated to JSON according to a fairly intuitive conversion.

|Python             |:arrow_right:|JSON  |
|        :---:      |    :---:    | :---:|
|dict	            |:arrow_right:|object|
|list, tuple	    |:arrow_right:|array |
|str	            |:arrow_right:|string|
|int, long, float	|:arrow_right:|number|
|True	            |:arrow_right:|true  |
|False	            |:arrow_right:|false |
|None	            |:arrow_right:|null  |

##### A Simple Serialization Example
Imagine you’re working with a Python object in memory that looks a little something like this:
```python
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
```
It is critical that you save this information to disk, so your mission is to write it to a file.
<br><br>
Using Python’s context manager, you can create a file called data_file.json and open it in write mode. <br>(JSON files conveniently end in a .json extension.)
```python
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
```
Note that dump() takes two positional arguments: 
1. the data object to be serialized
2. the file-like object to which the bytes will be written.

#### Some Useful Keyword Arguments
Remember, JSON is meant to be easily readable by humans, but readable syntax isn’t enough if it’s all squished together.
- indent paremeter: 
```python 
json.dump(x, indent=4)
```
- separators, >default value is (", ", ": "): 
```python
json.dump(x, indent=4, separators=(". ", " = "))
```
- Use the `sort_keys` parameter to specify if the result should be sorted or not: 
```python
json.dump(x, indent=4, sort_keys=True)
```
