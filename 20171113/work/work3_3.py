"""
有两个有序列表，[1，3，5，7，9]和[2，4，6，7，8]，
设计一个函数使两个数组合并，并且剔除掉两个数组里重复的元素。{1,2,3,4,5,6,7,8,9}
"""
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 7, 8]
# print(set(list1 + list2))
for i in set(list1 + list2):
    print(i, end=" ")

