import os

dict1 = {}

r1 = os.walk("C:\\Users\\Nikhil\\Documents\\Python_Assignments\\")
for r, d, f in r1:
    print(r)
    print(d)
    print(f)
    print("*"*10)
