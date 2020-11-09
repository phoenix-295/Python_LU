class letsup:
    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        print("Inside   ", self.First_Name)
        self.fullname = self.First_Name + self.Last_Name

    def email(self1):
        self1.email = self1.fullname+"@gmail.com"
        print(self1.email)


obj1 = letsup("Nikhil", "Hello", 90000)

obj2 = letsup("Chingi", "Pintu", 90000)

print(obj1.First_Name)

obj2.email()  # class.method(obj1) --> letsup.email(obj1)
