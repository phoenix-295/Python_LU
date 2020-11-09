from threading import Thread, Lock

list1 = []
lock = Lock()
k = 100


def fun1(a):
    global k
    lock.acquire()
    k = k-a
    list1.append(a)
    lock.release()


th1 = Thread(target=fun1, args=(10,))
th1.start()

th2 = Thread(target=fun1, args=(20,))
th2.start()

th1.join()
th2.join()

print("List is", list1)
