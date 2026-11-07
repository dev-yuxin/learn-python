# int 类型可以表示任意范围整数
num1 = 1

# 可以使用 _ 连接符表示大整数
num2 = 1_000_000_000

# 小整数池 [-5, 256] 里的整数对象是共享的
num1 = 100
num2 = 100
print(id(num1) == id(num2))
# 大整数 PyCharm 和非 PyCharm 环境执行结果会不一样
num1 = 1000
num2 = 1000
print(id(num1) == id(num2))
