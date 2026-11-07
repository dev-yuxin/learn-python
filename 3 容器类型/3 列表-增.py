list1 = []

# 尾插
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)

# 在指定索引处插入（索引越界会放到最左或最右）
list1.insert(1, 10)
print(list1)
list1.insert(-10, 0)
print(list1)

# extend() 就地拓展，传入一个可迭代对象
# extend([1, 2, 3]) 是把里面元素一个个就地尾插
# append([1, 2, 3]) 是直接把 [1, 2, 3] 作为一个元素就地尾插
# 列表相加是返回一个新列表，不是就地操作
list1.extend([1, 2, 3])
print(list1)
