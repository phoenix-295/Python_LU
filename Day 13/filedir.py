import os
from collections import defaultdict

d1 = {}
d2 = defaultdict(list)

r1 = os.walk("C:\\Users\\Nikhil\\Documents\\Python_Assignments")
for r, d, f in r1:
    for file in f:
        d1[file] = r

# print(d1)


fn = input("Enter filename :")

for k, v in d1.items():
    if fn in k.lower():
        print(k, "\t\t:  ", v)
