import copy
list1 = [[1, 2, 3], [10, 20, 30], [40, 45, 60]]
list2 = copy.copy(list1)
print("After Shallow Copy")
print("List 1 :", list1)
print("List 2 :", list2)
list1[2][0] = 35
print("After Changing value Copy")
print(list1)
print(list2)
print()

print("*"*50)

print()
list1 = [[1, 2, 3], [10, 20, 30], [40, 45, 60]]
list2 = copy.deepcopy(list1)
print("After Deep Copy")
print("List 1 :", list1)
print("List 2 :", list2)
list1[2][0] = 35
print("After Changing value Copy")
print(list1)
print(list2)
print("*"*50)
