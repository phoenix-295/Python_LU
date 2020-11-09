import time

t1 = "15-08-2020 15:20:30"


def hu_ep(t1):
    t11 = time.strptime(t1, "%d-%m-%Y %H:%M:%S")
    testtime = time.mktime(t11)
    return testtime


print(hu_ep(t1))
