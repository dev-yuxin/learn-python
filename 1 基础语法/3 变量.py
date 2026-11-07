# 变量就是用一个单词表示一个数据
# 本质上是数据是存内存里的，但内存地址使用不方便，使用变量名便于引用内存中的数据
# 你可以使用 id() 查看变量的内存地址
age = 18
print(id(age))

# 变量必须先初始化再使用
# print(name)  # 报错
name = "tom"
print(name)

# 同时初始化多个变量
a = b = c = 1
d, e, f = 1, 2, 3
print(a, b, c, d, e, f)

# 变量值可以修改，且变量不区分类型
# type() 可以查看变量类型
info = "hello world"
print(type(info))
info = 404
print(type(info))
info = [1, 2, 3]
print(type(info))

# 交换两个变量
num1 = 1
num2 = 2
print(num1, num2)
num1, num2 = num2, num1
print(num1, num2)
