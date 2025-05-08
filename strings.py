import pprint
pp = pprint.PrettyPrinter(indent=2)

first_name='Aquila'
last_name='Jedidiah'
team='Chelsea FC'
position='It is well'
age=23

# strings are also considered as part of the sequence family
print(first_name[2])
# slicing in python
print(last_name[0:4])
print(last_name[0:5])
print(last_name[0:6])
print(last_name[-2])

first_name_copy=first_name

# Everything is treaded as an object
# Helper methods

#memory address use id(value)
print(id(first_name))
print(id(first_name_copy))
print(id(last_name))
print(id(team))
print(id(position))
# if an object has the same memory address , then it means that the object is poinitnig to the same value in memory
#methods and attributes
# dir()
# help()
print(age)

#type use type(object)

pp.pprint(type(age))

pp.pprint(type(first_name))

course= "software engineering"
middle_name='Wafula Jedidiah'
print(list(middle_name))
# print(dir(course))


print(f"course :{course.capitalize()}")
print(f"course :{course.upper()}")
print(f"course :{course[::-1]}")
print(f"course :{course.count("e")}")
print(f"course :{course.count("s")}")
# Other string methods
"""
- isapha
- isalnum
- capitalize
-upper
-lower
-count
"""

print(("**************personal practice starts here**********").upper());
print(str("I am a string"))

#String interopolation
dog_name='Lucy'
print(f"say hello to my {dog_name}")