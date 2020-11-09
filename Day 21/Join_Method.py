from threading import Thread
import time
list1 = []

t1 = time.time()


def fun1(a, b):
    c = a+b
    time.sleep(3)
    list1.append(c)


th1 = Thread(target=fun1, args=(10, 20))
th1.start()

th2 = Thread(target=fun1, args=(50, 60))
th2.start()

th1.join()
th2.join()  # blocks termination of main thread till th2 finishes task
print("Final list is :", list1)
t2 = time.time()
print("Time taken :", t2-t1)
