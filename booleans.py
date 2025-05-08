# Booleans represent one of two values: True or false

# Syntax

x= True
y= False

print(x)
print(y)
# True and False are keywords in python
# The bool() function can be used to convert other data types to their boolean equivalents

# Boolean Evaluations
# Truthy an falsy values : Similar to JS, Python also has valyes that are considered truthy and falsy


# Falsy values
print(bool(0))
print(bool(""))
print(bool(None))

# Truthy values
print(bool(1))

print(bool("hello"))
print(bool([1, 2]))

# Boolean operators
#and, or , not are used to evaluate expressions
x=True
y=False

print(x and y)
print(x or y)
print(not x)