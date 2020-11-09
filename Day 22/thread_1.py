from threading import Thread
import time


def fun1():
    print("Inside Deamon")
    time.sleep(4)
    print("Exiting the Daemon")


def fun2():
    print("Inside non Deamon")
    time.sleep(3)
    print("Exiting the non Daemon")


th1 = Thread(target=fun1)
th1.setDaemon(True)
th2 = Thread(target=fun2)

th1.start()
th2.start()
