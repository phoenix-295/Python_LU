import copy
list1 = [[1, 2, 3], [10, 20, 30], [40, 45, 60]]
# list2 = copy.deepcopy(list1)
list2 = copy.copy(list1)
print("List 1 :", list1)
print("List 2 :", list2)
list1[2][0] = 35
print(list1)
print(list2)
