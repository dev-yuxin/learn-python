# python 中所有数据类型都是对象类型，哪怕是一个简单整数也是对象。

# 内置基础数据类型
# int(整数)
# float(浮点数)
# bool(布尔)
# str(字符串)
# list(列表)
# set(集合)
# tuple(元组)
# dict(字典)
# None

# 需要导包的数据类型
# decimal.Decimal
# datetime.datetime
# ...

# 自定义对象

# 你可以使用 type() 查看变量的数据类型
print(type(1))

# 你可以使用 isinstance() 判断变量或值属不属于某个数据类型（或属于其子类型）
# 内置基础数据类型里面只有 bool 是 int 的子类型
print(isinstance(True, int))  # True
print(isinstance(1, bool))  # False
print(isinstance(1, float))  # False
print(isinstance("1", int))  # False
