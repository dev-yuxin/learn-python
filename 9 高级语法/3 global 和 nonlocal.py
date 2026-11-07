# python 中的作用域
# 内置作用域，不管哪里跨模块都能用，比如 print(), max() 等。
# 全局作用域，整个.py模块中可以使用。
# 局部作用域：定义函数时就会创建局部作用域。如果函数嵌套，那么分别对应内层函数的局部作用域和外层函数的嵌套作用域。
# if，for, while, try 等不会产生局部作用域，只有函数（包括lambda函数）、类、推导式会产生作用域。

# 名字查找顺序：从内层向外层查找，内层局部作用域 => 外层嵌套作用域 => 全局作用域 => 内置作用域 => 找不到报错
# 内层作用域会按名字查找顺序读外层作用域的变量
# 如果你在内层想读指定作用域里的名字，你需要显示声明 global, nonlocal 。
# 如果你在内层想对外层变量进行写操作，且写操作会改变地址值，你必须显示声明 global, nonlocal 。就地写操作可省略，但最好还是显示声明。

# 全局作用域
a = 1
b = 1


# 读操作
def read():
    # 外层嵌套作用域
    b = 2

    def inner():
        # 内层局部作用域
        c = 3
        print(c)
        print(b)
        print(a)

    inner()


read()

list1 = [1]
list2 = [1]


# 写操作
def write():
    # 就地修改全局作用域下的 list1（因为不改变list1地址值，声明作用域语句是可省略的）
    # global list1
    list1.append(2)
    # 在嵌套作用域下定义一个 list2，不影响全局作用域里的 list2
    list2 = [1, 2]

    def inner():
        # 修改嵌套作用域下的 list2（list2地址值可能改变，声明作用域语句不能省略）
        nonlocal list2
        list2 += [3]
        print(list2)

    inner()


write()
print(list1)
print(list2)
