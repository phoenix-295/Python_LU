from multiprocessing import Process, current_process
import time

def call_name(name):
    print(name, current_process().name, current_process().pid)
    time.sleep(5)
    print("Done")


if __name__ == "__main__":

    p2 = Process(name="Worker", target=call_name, args=("Hello",))
    p2.start()
    print("before kill ",p2.is_alive())
    time.sleep(2)
    p2.terminate()
    p2.join()
    print("After kill ",p2.is_alive())