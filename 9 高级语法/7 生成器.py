import random


# 生成器是特殊的迭代器
# 普通迭代器对象是由 __iter__() 返回的，生成器对象则是由含有 yield 的函数返回，或者是生成器推导式创建。
# 普通迭代器对象需要自己去实现 __next__() 方法，生成器对象已经实现了。
# 生成器除了 __next__ 方法，还有一个 send 方法。

# return 是直接返回值，并且结束
# 含有 yield 后，函数调用不再是执行函数体，而是返回一个生成器对象。
# 第1次调用 next() 函数体开始执行，执行到 yield 1中断，next() 返回 1
# 第2次调用 next() 从中断处恢复执行，执行到 yield 2中断，next() 返回 2
# ...
def f1():
    print("f1开始执行")
    yield 1
    yield 2
    yield 3
    print("f1执行结束")


g = f1()
print(type(g))
for item in g:
    print(item)

# 列表推导式: [推导式]
# 集合推导式: {推导式}
# 字典推导式: {k:v 推导式}
# 没有元组推导式，(推导式) 这是生成器推导式
g = (item for item in range(5))
print(type(g))
for item in g:
    print(item)

# my_range() 不执行函数体，返回一个生成器对象
# 第1次执行 send(None) 第1次必须传None因为没有变量接收它，函数体执行到 yield my_list 中断，send() 返回 my_list，此时左侧的 step = 还没执行。
# 第2次执行 send(n)，从中断处恢复执行，step = n 进行赋值操作（兼容None），继续执行到 yield my_list 中断，send(n) 返回 my_list，此时左侧的 step = 还没执行。
# ...
def my_range(start, end):
    my_list = []
    i = start
    while i < end:
        my_list.append(i)
        step = yield my_list
        step = step if step else 1
        i += step


g = my_range(1, 10)
my_list = g.send(None)
print(f"当前序列: {my_list}")
while True:
    try:
        step = random.randint(1, 3)
        my_list = g.send(step)
        print(f"步长: {step}, 当前序列: {my_list}")
    except StopIteration:
        break

