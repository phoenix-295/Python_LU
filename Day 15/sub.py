import re

str1 = "what we think we become "
p = "we"

repl = re.sub(p, "I", str1, 1)

print(repl)
