# 可迭代对象：
# 可迭代对象要求实现 __iter__() 方法，该方法返回一个迭代器对象。
# 内置函数 iter(可迭代对象) 等价于 可迭代对象.__iter__()

# 迭代器对象：
# 迭代器对象要求去实现 __next__() 方法，该方法返回遍历过程中的元素。
# 内置函数 next(迭代器对象) 等价于 迭代器对象.__next__()
# 迭代器不能回头，用完就没了，想再次遍历得创建一个新的迭代器

list1 = [1, 2, 3]

my_iter = list1.__iter__()
while True:
    try:
        print(my_iter.__next__())
    except StopIteration as e:
        break

my_iter = iter(list1)
while True:
    try:
        print(next(my_iter))
    except StopIteration as e:
        break

# for-in 本质就是上面的语法糖
for item in list1:
    print(item)
