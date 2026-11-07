# 字面量创建集合
set1 = {"h", "e", "l", "l", "o"}
print(set1)

# 创建空集合
# {} 是空字典
set1 = set()
print(set1)

# 把可迭代对象转为集合
set1 = set("hello world")
print(set1)

# 添加元素
set1 = set()
for letter in "hello world":
    set1.add(letter)
print(set1)

# 删除元素（元素不存在会报错）
set1 = {10, 20, 30, 40, 50}
set1.remove(20)
print(set1)

# 删除并返回遍历顺序第0位的元素（因为无序，不确定第0位存的谁），无法指定索引
set1 = {10, 20, 30, 40, 50}
item = set1.pop()
print(item, set1)

# 清空集合
set1 = {10, 20, 30, 40, 50}
set1.clear()
print(set1)

# 遍历只能用 for-in，无法使用索引
set1 = {10, 20, 30, 40, 50}
for item in set1:
    print(item, end=" ")
else:
    print()

# 并集
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50}
# | 并集，返回新集合
set3 = set1 | set2
print(set3)
# union() 并集，返回新集合
set4 = set1 | set2
print(set4)
# update() 并集，就地更新，返回None
set1.update(set2)
print(set1)

# 交集
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50}
# & 交集，返回新集合
set3 = set1 & set2
print(set3)
# intersection 交集，返回新集合
set4 = set1.intersection(set2)
print(set4)
# intersection_update 交集，就地更新，返回None
set1.intersection_update(set2)
print(set1)

# 差集
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50}
# - 差集，返回新集合
set3 = set1 - set2
print(set3)
# difference 差集，返回新集合
set4 = set1.difference(set2)
print(set4)
# difference_update 差集，就地更新，返回None
set1.difference_update(set2)
print(set1)

# issubset() 是否是子集
# issuperset() 是否是父集
set1 = {10, 20, 30, 40}
set2 = {20, 30}
print(set1.issuperset(set2))
print(set2.issubset(set1))
