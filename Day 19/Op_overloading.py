class letsup:
    incf = 1.40

    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        self.full_name = self.First_Name + self.Last_Name
        print("Inside  Parent ", self.First_Name)

    def __add__(self, other):
        return self.sal + other.sal

    def __gt__(self, other):
        return self.sal > other.sal

    def __len__(self):
        return len(self.full_name)

    # def email1(self):
    #     self.email1 = self.full_name+"@gg"
    #     print(self.email1)


obj1 = letsup("Nikhil", "Hello", 90000)
obj2 = letsup("Chingi", "Pintu", 80000)

print(obj1 + obj2)
print(obj1 > obj2)
print(len(obj1))
