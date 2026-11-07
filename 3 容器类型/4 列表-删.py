list1 = [10, 20, 20, 30, 40, 50, 60, 70, 80, 90]

# 根据值删除元素（只删从左往右首次出现的第一个）
list1.remove(20)
print(list1)

# 根据索引删除
del list1[-1]
print(list1)

# 根据切片删除
del list1[-2:]
print(list1)

# 根据索引删除并返回元素（默认是最后一个）
item = list1.pop()
print(item, list1)
item = list1.pop(0)
print(item, list1)

# 清空列表
list1.clear()
print(list1)
