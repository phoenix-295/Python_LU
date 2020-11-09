import re

str1 = "abc jsdhs6!#@&*&#$&#$&  dse4343 423fd"

p = r"[^a-zA-Z0-9]"

np = re.sub(p, "", str1)

print(np)
