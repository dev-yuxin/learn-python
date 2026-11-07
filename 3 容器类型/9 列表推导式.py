import random

# 生成一个列表 [1^2, 2^2, ... 5^2]
list1 = [item ** 2 for item in range(1, 6)]
print(list1)

# 产生10个[1, 100]随机数的列表
list1 = [random.randint(1, 100) for i in range(10)]
print(list1)

# 生成一个1~20的列表，排除3的倍数
list1 = [item for item in range(1, 21) if item % 3 != 0]
print(list1)

# 列表推导式中嵌套循环
list1 = [(i, j) for i in range(1, 3) for j in range(2, 5)]
print(list1)

# 列表删除所有为3的元素
list1 = [1, 2, 3, 3, 3, 1]
list2 = [item for item in list1 if item != 3]
print(list2)
# 方法二，注意删除时会把列表长度和原来的索引值改变
index = 0
while index < len(list1):
    if list1[index] == 3:
        del list1[index]
    else:
        index += 1
print(list1)
