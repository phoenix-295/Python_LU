class letsup:
    incf = 1.40

    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        self.full_name = self.First_Name + self.Last_Name

    def incr(self):
        self.sal = self.sal*letsup.incf
        print(self.sal)

    @classmethod
    def inc(cls, amt):
        cls.incf = amt


obj1 = letsup("Nikhil", "Hello", 90000)
obj2 = letsup("Chingi", "Pintu", 50000)
# obj1.inc(1.5)
obj1.incr()
obj2.incr()

# print(obj1.incr())
