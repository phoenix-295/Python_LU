from threading import Thread
from queue import Queue

q1 = Queue()


def fun1():
    while True:
        print(q1.get())
        q1.task_done()
        print("Unfinishehd task:", q1.unfinished_tasks)


th1 = Thread(target=fun1)
th1.setDaemon(True)
th1.start()

for each in range(1, 6):
    q1.put(each)

q1.join()
