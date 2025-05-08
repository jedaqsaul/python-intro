# integers and floats
# integers are whole numbers like 1, 42 or 7
# floats are decimal numbers like 3.14, 0.5 and so forth
print(type(7))
print(type(5.4))

# You can also covert between integers and float

print(int("1"))
print(int(1.9))
print(int(float("1.1")))
print(float("1.1"))
# division and float behaviour

print(4/3)
print(4/3.0)
print(float(4/3))
print(int(4/3))

# Even when using two integers, Python returns a float for /. 
# For integer division, Python has a special operator: 
# // (try 4 // 3, which returns 1).

print(4//3)