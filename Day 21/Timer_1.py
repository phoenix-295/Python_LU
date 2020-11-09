from threading import Timer


def fun1(a, b):
    print(a+b)


Timer(4, fun1, args=(10, 20)).start()
