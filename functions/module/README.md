#### Import Module
-	A module is compiled of any number of functions
-	The module allows us to write our own set of functions and share them 
-	The syntex of a writing a module is exactly the same as writing ordinary functions
*	syntex: `import module_name`
*	use:	`module_name.func_name_in_module(func_args)`


#### Import Function
-	Just like importing an entire module, we can also import a specific functions from a module
*	syntex: `import func_name_in_module from module_name`
*	use:	`func_name_in_module(func_args)`

#### Module alias
-	We can call a module by different name (alias) instead of the original name
-	This can make our life easier at calling the module in our main program
* syntex: 'import module_name as module_alias'

#### Function alias
- We can call a function by different name (alias) instead of the original name
  - This can help us in cases:
    - the orginal function name is too long or complicated
    - there is already a function in that name
    - etc...
- syntex: `import func_name_in_module from module_name as func_alias`
