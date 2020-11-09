from multiprocessing import Process

def call_name(name):
    print("Hello ", name)

p = Process(target=call_name, args=("Nikhil",))
p.start()
