from threading import Thread


def fun1(a, b):
    c = a+b
    print(c)


th1 = Thread(target=fun1, args=(10, 20))
th1.start()

th2 = Thread(target=fun1, args=(50, 60))
th2.start()
