from multiprocessing import Process, current_process
import time

def call_name(name):
    print(name, current_process().name, current_process().pid)
    time.sleep(4)
    print("Done")


if __name__ == "__main__":

    p = Process(target=call_name("Nikhil"))
    p.start()

    p2 = Process(target=call_name, args=("Hello",))
    p2.start()
