class letsup:
    incf = 1.40

    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        self.full_name = self.First_Name + self.Last_Name
        print("Inside  Parent ", self.First_Name)

    def email1(self):
        self.email1 = self.full_name+"@gg"
        print(self.email1)


class tr(letsup):
    def __init__(self, first, last, pay, sub):
        # letsup.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.subject = sub
        print("Inside  child ")


obj1 = tr("Nikhil", "Hello", 90000, "Python")
obj2 = tr("Chingi", "Pintu", 90000, "hello")

obj1.email1()
