from threading import Thread, current_thread
import time
list1 = []

t1 = time.time()


def fun1(a, b):
    c = a+b
    time.sleep(3)
    list1.append(c)
    print("Current Thread", current_thread())


list_t = []
for each in range(5):
    th1 = Thread(target=fun1, args=(10, each))
    th1.start()
    list_t.append(th1)
    # th1.join()
for th in list_t:
    th.join()

print("Final list is :", list1)
t2 = time.time()
print("Time taken :", t2-t1)
