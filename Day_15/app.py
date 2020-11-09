import re

str1 = "we become what WE think"
p = "we"

iter1 = re.finditer(p, str1, re.I)

for m in iter1:
    print(m)

# if m:
#     print(m.group(), m.start(), m.end())
