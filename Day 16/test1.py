import re

str1 = "abc jsdhs6 dse4343 423fd"

p = r"[a-zA-Z0-9]"

iter1 = re.finditer(p, str1)

for m in iter1:
    print(m.group(), m.start())
