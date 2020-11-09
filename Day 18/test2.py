class letsup:
    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        print("Inside   ", self.First_Name)

    def full(self):
        self.fullname = self.First_Name + self.Last_Name

    def email1(self):
        self.email = self.fullname+"@gmail.com"
        print(self.email)


obj1 = letsup("Nikhil", "Hello", 90000)

obj2 = letsup("Chingi", "Pintu", 90000)


obj2.full()
obj2.email1()  # class.method(obj1) --> letsup.email(obj1)
