class letsup:
    incf = 1.40

    def __init__(self, first, last, pay):
        self.First_Name = first
        self.Last_Name = last
        self.sal = pay
        self.full_name = self.First_Name + self.Last_Name
        print(self.full_name)

    @classmethod
    def alt(cls, str1):
        a, b, c = str1.split()
        return cls(a, b, int(c))


str1 = "Nikhil S 90000"
str2 = "Chingi P 50000"

obj1 = letsup.alt(str1)
obj2 = letsup.alt(str2)
