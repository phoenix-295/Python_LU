import multiprocessing
import time


def shared(v):
    v.value + 1
    print("Value is:", v.value)


val = multiprocessing.Value('1', 10)

list1 = []
for each in range(5):
    p = multiprocessing.Process(target=shared, args=(val,))
    p.start()
    list1.append(p)
time.sleep(2)

for p in list1:
    p.join()

print("In the end ", val.value)
