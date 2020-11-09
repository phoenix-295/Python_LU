import re

str1 = "Hello world!!"
p = "world"

m = re.search(p, str1)

print(m)

if m:
    print(m.group(), m.start(), m.end())
