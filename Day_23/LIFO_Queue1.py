from queue import LifoQueue


q1 = LifoQueue()
for each in range(1, 6):
    q1.put(each)

while not q1.empty():
    print(q1.get())
