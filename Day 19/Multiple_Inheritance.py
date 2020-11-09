class A:
    def sum1(self, a, b):
        c = a+b
        print(c)


class B:
    def sum1(self, a, b):
        c = a-b
        print(c)


class C(A, B):
    pass


obj1 = C()

obj1.sum1(10, 10)
# obj1.sum1(10, 5)
