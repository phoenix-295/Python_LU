import random
import string


def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_int():
    res_str = ""
    x = range(4)
    for n in x:
        a = random.randint(0, 9)
        res_str = res_str + str(a)
    return res_str


def get_random_pun(length):
    letters = string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def listToString(s):
    str2 = ""
    for ele in s:
        str2 += ele

    return str2


str1 = get_random_string(6)

str2 = get_random_int()

str3 = get_random_pun(2)


list1 = []
for each in str1:
    list1.append(each)

for each in str2:
    list1.append(each)

for each in str3:
    list1.append(each)

a = random.sample(list1, len(list1))

final_pass = listToString(a)
print(final_pass)
