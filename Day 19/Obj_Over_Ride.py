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

    def __str__(self):
        return("The Object belongs to me!")


obj1 = letsup("Nikhil", "Hello", 90000)
obj2 = letsup("Chingi", "Pintu", 80000)

print(obj1)
