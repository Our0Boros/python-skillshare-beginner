## unittest

#### What is Unit Testing?
Unit Testing is the first level of software testing where the smallest testable parts of a software are tested. <br> This is used to validate that each unit of the software performs as designed.<br>
The unittest test framework is python’s xUnit style framework.

- #### test fixture:
A test fixture is used as a baseline for running tests to ensure that there is a fixed environment in which tests are run so that results are repeatable.
- Examples :
  - creating temporary databases.
  - starting a server process.
- #### test case:
A test case is a set of conditions which is used to determine whether a system under test works correctly.
- #### test suite:
Test suite is a collection of testcases that are used to test a software program to show that it has some specified set of behaviours by executing the aggregated tests together.
- #### test runner:
A test runner is a component which set up the execution of tests and provides the outcome to the user.

#### Basic Test Structure :
unittest defines tests by the following two ways :

- Manage test “fixtures” using code.
- test itself.
```python
import unittest 
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):         
        self.assertTrue(True) 
  
if __name__ == '__main__': 
    unittest.main() 
```
This is the basic test code using unittest framework, which is having a single test. <br>
This test() method will fail if TRUE is ever FALSE.

```python
if __name__ == '__main__':
    unittest.main()
```
- This last block helps to run the test by running the file through the command line.

The result of this test:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
- The 1 dot ".", indicates that 1 test was ran.

#### Outcomes Possible :
There are three types of possible test outcomes :

- OK – This means that all the tests are passed.
- FAIL – This means that the test did not pass and an AssertionError exception is raised.
- ERROR – This means that the test raises an exception other than AssertionError.

#### Python code to demonstrate working of unittest 
```python
import unittest 

class TestStringMethods(unittest.TestCase): 
	
	def setUp(self): 
		pass

	# Returns True if the string contains 4 a. 
	def test_strings_a(self): 
		self.assertEqual( 'a'*4, 'aaaa') 

	# Returns True if the string is in upper case. 
	def test_upper(self):		 
		self.assertEqual('foo'.upper(), 'FOO') 

	# Returns TRUE if the string is in uppercase 
	# else returns False. 
	def test_isupper(self):		 
		self.assertTrue('FOO'.isupper()) 
		self.assertFalse('Foo'.isupper()) 

	# Returns true if the string is stripped and 
	# matches the given output. 
	def test_strip(self):		 
		s = 'hello world'
		self.assertEqual(s.strip('hell'), 'o world') 

	# Returns true if the string splits and matches 
	# the given output. 
	def test_split(self):		 
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world']) 
		with self.assertRaises(TypeError): 
			s.split(2) 

if __name__ == '__main__': 
	unittest.main() 
```
The above code is a short script to test 5 string methods. <br>
`unittest.TestCase` is used to create test cases by subclassing it. <br>
The last block of the code at the bottom allows us to run all the tests just by running the file.

- The output of those tests:
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```
##### Basic terms used in the code :

- assertEqual() – This statement is used to check if the result obtained is equal to the expected result.
- assertTrue() / assertFalse() – This statement is used to verify if a given statement is true or false.
- assertRaises() – This statement is used to raise a specific exception.

Description of tests :

- test_strings_a
This test is used to test the property of string in which a character say ‘a’ multiplied by a number say ‘x’ gives the output as x times ‘a’. <br>
The `assertEqual()` statement returns true in this case if the result matches the given output.
- test_upper
This test is used to check if the given string is converted to uppercase or not. <br>
The `assertEqual()` statement returns true if the string returned is in uppercase.
- test_isupper
This test is used to test the property of string which returns TRUE if the string is in uppercase else returns False. <br>
The `assertTrue()` / `assertFalse()` statement is used for this verification.
- test_strip
This test is used to check if all chars passed in the function have been stripped from the string. <br>
The `assertEqual()` statement returns true if the string is stripped and matches the given output.
- test_split
This test is used to check the split function of the string which splits the string through the argument passed in the function and returns the result as list. <br>
The `assertEqual()` statement returns true in this case if the result matches the given output.

