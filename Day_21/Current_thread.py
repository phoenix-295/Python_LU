from threading import Thread, active_count, current_thread, enumerate
import time


def fun1(a, b):
    print("Current :", current_thread())
    time.sleep(2)
    c = a+b
    print(c)


th1 = Thread(target=fun1, args=(10, 20))
th1.start()

th2 = Thread(target=fun1, args=(50, 60))
th2.start()

print("Total threads :", active_count())
print("List is :", enumerate())
