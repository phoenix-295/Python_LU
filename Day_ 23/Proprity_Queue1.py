from queue import PriorityQueue


q1 = PriorityQueue()
q1.put((1, "Admin"))
q1.put((10, "Nikhil"))
q1.put((8, "Hello"))

while not q1.empty():
    print(q1.get()[1])
