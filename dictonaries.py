# A dictionary in python is an unordered collection of key-value pairs. 
# Dictornaries care created with curly braces{}, where each key maps to a value


# Syntax
my_dict={"key1": "value1", "key2": "value2"}
print(my_dict)

# key characteristics
# Unordered- No guarantee of element order
# Indexed by keys- You can access values by their associated keys(not indices)
# Keys must be immutable- You cant use a list or a set a s a key, but strings, numbers and tuples are fine
# Values can be anything: You can stors a variety of data types as values


my_dict={"key1": 1, "key2":2}
print(my_dict["key1"])
print(my_dict["key2"])

# You can use .get() to safely access a key
print(my_dict.get("key3"))# you will get none if key does not exist

# Common dictonary methods
my_dict={"a":1, "b":2, "c":3}
# Adding a new key value pair
my_dict["d"]=4
# Removing a key -value pair
del my_dict["b"]
print(my_dict)
# Getting all keys/values
keys=my_dict.keys()
values=my_dict.values()
print(keys, values)
# checking if a key exists
print("a" in my_dict)