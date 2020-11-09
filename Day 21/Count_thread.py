from threading import Thread, active_count, enumerate
import time


def fun1(a, b):

    c = a+b
    print(c)


th1 = Thread(target=fun1, args=(10, 20))
th1.start()

th2 = Thread(target=fun1, args=(50, 60))
th2.start()

time.sleep(2)
print("Total threads :", active_count())
print("List is :", enumerate())
