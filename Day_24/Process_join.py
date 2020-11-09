from multiprocessing import Process
import time

t1 = time.time()


def call_name(name, num1):
    time.sleep(2)
    print("Hello ", name, num1)


list1 = []
for each in range(1, 5):
    p = Process(target=call_name, args=("Nikhil", each))
    p.start()
    list1.append(p)

for p in list1:
    p.join()

t2 = time.time()

print("Time taken :", t2-t1)
