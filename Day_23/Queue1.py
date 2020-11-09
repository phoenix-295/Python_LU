from queue import Queue


q1 = Queue()  # FIFO queue
for each in range(1, 6):
    q1.put(each)

print(q1.get())
