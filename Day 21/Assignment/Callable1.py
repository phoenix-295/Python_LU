from collections import Counter


class MyCounter(Counter):
    def __call__(self, c1):
        count1 = Counter(c1)
        print(count1)


co1 = MyCounter()
co1("Hello")
