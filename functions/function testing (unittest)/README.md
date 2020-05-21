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
