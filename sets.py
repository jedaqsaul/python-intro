# A set is an unorderd, unindexed and unchangable (per item) colleciton of unique value
# syntax- you can create a set using curly braces{} or the set() constructor
my_set={1, 2,3, 4, 5,6, 3,2,3,2}
print(my_set)
# Duplicates for each value are removed
another_set=set([7, 6, 6, 7, 4, 3])
print(another_set)


# Unordered- No guarantee of element order
# Unindexed- can access items by index(my_set[0] causes an error)
# Unique- Duplicate values are automatically removed
# Unchangable per Item- You cant update an element, but you can add or remove entire items

# Below are common set methods
s={1, 2, 3}
print(s)
s.add(4)

print(s)
s.remove(2)
print(s)

s.discard(5) # safe remove, no error
print(s)
s.pop()
print(s)
s.clear()
print(s)