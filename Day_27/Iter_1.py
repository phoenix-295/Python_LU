sampleList = [1, 2, 3]
# Making the sampleList iterable using iter() which returns an iterator.
newlist = iter(sampleList)

print("Sample is:", sampleList)

print("Iter is :", next(newlist))
print("Iter is :", next(newlist))
