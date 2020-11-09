import os
import re

list1_files = os.listdir("D:\Transfer\X6\Setups")

p = r"[0-9]"

for file in list1_files:
    m = re.search(p, file)
    if m:
        print(m.group())
