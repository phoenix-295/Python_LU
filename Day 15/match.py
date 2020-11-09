import re

str1 = "Hello world!!"
p = "he"

m = re.match(p, str1)

print(m)

if m:
    print(m.group(), m.start(), m.end())
