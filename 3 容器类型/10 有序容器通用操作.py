# 有序容器（列表，字符串，元组）的通用操作

# 切片和索引
str1 = "hello world"
print(str1[-2])
print(str1[-2:])

# index()
str1 = "hello world"
# 从左往右找首次出现的索引，找不到报错
print(str1.index("l"))
# 指定[start, end)范围查找
print(str1.index("o", 6, -1))
print(str1.index("l", 6))

# + 拼接
# * 重复多少次
list1 = [1, 2, 3]
list2 = [4, 5]
print(list1 + list2)
print(list1 * 3)

# count() 统计次数
print(str1.count("l"))

# 遍历
for letter in str1:
    print(letter)
for index in range(len(str1)):
    print(str1[index])
for index, letter in enumerate(str1):
    print(index, letter)
