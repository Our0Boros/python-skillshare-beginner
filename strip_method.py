address = "101 Main Street"
print(address)#The usual

address_2 = "		102 Main Street   "
print(address_2.lstrip())

address_3 = "	  	103 Main Street   ".rstrip()
print(address_3)

address_4 = "		104 Main Street   ".strip()
print(address_4)

#The .strip() function strips the 'spaces (whitespace) and tabs'
#at the beginning and the end of a string

#.strip() clean all whitespace

#.lstrip() clean whitespace on the left side

#.rstrip() clean whitespace on the right side

#The .strip() method can be applied to the string itself or the print command as shown
