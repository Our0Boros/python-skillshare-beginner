### 15/04/2020
### Author: Omer Goder
### Creating a list of numbers

# Convert numbers into a list
numbers = list(range(1,6))
print(numbers)
print('\n')

# print("List of even number in the range of 0 to 100:")
even_numbers = list(range(0,102, 2))
print(even_numbers)
print('\n')

print("List of square values of 1 to 10:")
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)
print('\n')

digits = [1,2,3,4,5]
print(min(digits))
print(max(digits))
print(sum(digits))

print('\n')
