import time

t1 = time.time()


def count(n):
    i = n
    while i > 0:
        i = i - 1


count(100000000)
t2 = time.time()

print("Time :", t2-t1)
