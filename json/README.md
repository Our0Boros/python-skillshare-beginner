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
|        :---:      |:arrow_right:|| :---:|
|dict	            |:arrow_right:||object|
|list, tuple	    |:arrow_right:||array |
|str	            |:arrow_right:||string|
|int, long, float	|:arrow_right:||number|
|True	            |:arrow_right:||true  |
|False	            |:arrow_right:||false |
|None	            |:arrow_right:||null  |

