class letsup:

    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        self.full_name = self.First_Name + self.Last_Name

    @property
    def mail1(self):
        self.email = self.full_name+"@hh.com"
        print(self.email)

    @mail1.setter
    def mail1(self, value):
        self.full_name = value


obj1 = letsup("Nikhil", "Hello", 90000)
obj2 = letsup("Chingi", "Pintu", 50000)

print(obj1.mail1)
obj1.mail1 = "nik@let.com"
print(obj1.mail1)
