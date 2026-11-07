list1 = [1, 2, 3, 4, 5]

# 直接 for in 遍历
for item in list1:
    print(item, end=" ")
else:
    print()

# 根据索引遍历
for index in range(len(list1)):
    print(list1[index], end=" ")
else:
    print()

# enumerate 同时遍历索引和元素，拿到的是一个 (index，item) 组成的二元组
for index, item in enumerate(list1):
    print("索引", index, "元素", item)
