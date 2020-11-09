from multiprocessing import Process, current_process
import time

def call_name(name):
    print(name, current_process().name, current_process().pid)
    print("Done")


if __name__ == "__main__":

    p = Process(target=call_name, args=("Nikhil",))
    p.start()

    p2 = Process(name="Worker", target=call_name, args=("Hello",))
    p2.start()
