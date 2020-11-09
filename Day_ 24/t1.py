from multiprocessing import Process, current_process
import time

list1 = []


def call_name(name):
    # print(name, current_process().name, current_process().pid)
    list1.append(name)
    print(current_process().name, list1)


if __name__ == "__main__":

    p = Process(target=call_name, args=("Nikhil",))
    p.start()

    p2 = Process(target=call_name, args=("Hello",))
    p2.start()

    p.join()
    p2.join()

    time.sleep(2)
    print("List :", list1)
