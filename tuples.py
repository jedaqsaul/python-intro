# A tuple is an ordered, immutable collection. 
# Once created , the contents of a tuple cannot be changed
# Tuples use parentheses() instead of square brackets

my_tuple=(1, 2, 3)
print(type(my_tuple))

# You can also use the tuple() constructor to convert a list into a tuple
print(tuple([1, 2, 3]))
# You must include a comma when creating a tuple with a single item

single=(1, )
print(single)
print(type(single))
# Why typles matter
# Immutable- You cannot use .pop() or .append() on them
# Use cases- Ideal for fixed data, like coordinates, 
# or database query results where immutablity is important


tuple_string=('Aquila', 'jedidiah', 'wafula')
print(tuple_string)
print(type(tuple_string))