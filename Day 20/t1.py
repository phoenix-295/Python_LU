class letsup:

    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        self.full_name = self.First_Name + self.Last_Name

    def __call__(self, first):
        self.full_name = first

    def mail1(self):
        self.email = self.full_name+"@hh.com"
        print(self.email)


obj1 = letsup("Nikhil", "Hello", 90000)
obj2 = letsup("Chingi", "Pintu", 50000)

obj1("Nikhil")

# obj1.mail1
# obj1("nik12")
# obj1.mail1()
