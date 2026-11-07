# 元组：不可变，有序，元素可重复
# 元组不能进行增、删、改等涉及写的操作，只能进行读操作

# 字面量形式创建元组
tuple1 = (1, 2, 3)
print(tuple1)

# 如果只有一个元素必须写,
tuple1 = (1,)
print(tuple1)

# 空元组
tuple1 = ()
print(tuple1)
tuple2 = tuple()
print(tuple2)

# 将一个可迭代对象转为 tuple
tuple1 = tuple("hello")
print(tuple1)

# 这里 sorted() 传入的元组不会改变，返回一个排序后的列表
tuple1 = (1, 2, 1, 3, 2)
list1 = sorted(tuple1)
print(tuple1)
print(list1)
