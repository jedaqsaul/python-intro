# A list in python is an ordered collectoin of items
# It can hold any type of data,
# And is created using square brackets []
from pprint import pp
numbers=[1, 3, 455, 5]
print(type(numbers))
print(numbers)

# You can also use the list() constructor
empty =list()
print(type(empty))
print(empty)

# Accessing elements by index (just like JS arrays)
list_abc =['a', 'b', 'c', 'd']
print(list_abc[0])
print(list_abc[1])
print(list_abc[2])
print(list_abc[3])

# List functions
pp(dir(list_abc))

print(len(list_abc))
print(sorted([1, 3, 455, 5]))

list_123=[1,2,3]
print(list_123.pop()) #removes and returns the last element
print(list_123.remove(1))
print(list_123)

# LIst are mutable which means you can change their contents
