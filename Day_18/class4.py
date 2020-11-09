class letsup:
    incf = 1.40

    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        print("Inside   ", self.First_Name)

    def increm(self):
        self.sal = self.sal*letsup.incf


obj1 = letsup("Nikhil", "Hello", 90000)
obj2 = letsup("Chingi", "Pintu", 90000)

print("before calling pay", obj1.sal)

obj1.increm()
print("After calling pay", obj1.sal)
