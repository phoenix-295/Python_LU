import time
from threading import Thread
import os
from collections import defaultdict
import pickle

list1 = ["C:\\", "D:\\"]
dict1 = defaultdict(list)


def fun1(Drive):
    resp = os.walk(Drive)
    for r, d, f in resp:
        for file in f:
            dict1.setdefault(file, []).append(r)


t1 = time.time()
for each in list1:
    th1 = Thread(target=fun1(each))
    th1.start()
    # fun1(each)
th1.join()
t2 = time.time()

print("Time Taken :", t2-t1)

file_r = open("file.dump", "wb")
pickle.dump(dict1, file_r)
file_r.close()
