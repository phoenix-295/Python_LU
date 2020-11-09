from threading import Thread, current_thread
import time


def fun1(a, b):
    time.sleep(4)
    print("Current :", current_thread())
    c = a+b
    print(c)


th1 = Thread(target=fun1, args=(10, 20))
th1.start()
th1.join(3)  # tell to main thread to block main thread it 3 secs

print("Finally Done", th1.is_alive())
