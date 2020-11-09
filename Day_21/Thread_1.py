from threading import Thread


class MyThread(Thread):
    def __init__(self, value):
        Thread.__init__(self)
        self.value = value

    def run(self):
        print(self.value)


th1 = MyThread(20)
th1.start()

th2 = MyThread(30)
th2.start()
