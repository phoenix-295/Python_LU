class A:
    def sum1(self, a, b):
        c = a+b
        print(c)


class B(A):
    pass


class C(B):
    pass


obj1 = C()

obj1.sum1(10, 10)
