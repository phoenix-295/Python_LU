import os
from collections import defaultdict

d1 = {}
d2 = defaultdict(list)

r1 = os.walk("D:\\")
for r, d, f in r1:
    for file in f:
        d2.setdefault(file, []).append(r)

fn = input("Enter File name:")
print("*"*50)

for k, v in d2.items():
    if fn in k.lower():
        print(k+'\t'+'\n{0}\t'.format(k).join(v))
print("*"*50)
