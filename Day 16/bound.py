import re

list1 = ["intel", "intel123", "intel#", "(intel)"]

p = r"\bintel\b"

for each in list1:
    m = re.search(p, each)
    if m:
        print(m.group(), each)
    else:
        print("Not matched")
