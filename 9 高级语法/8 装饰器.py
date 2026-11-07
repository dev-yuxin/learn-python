# 装饰器是一个特殊函数，用于包装另一个函数，返回一个包装后的新函数
# 装饰器可以在不修改原函数的基础上拓展功能

# 装饰器函数，兼容字符串型
# 外层函数参数接收原函数
def format_float(f):
    # 内层函数参数必须和原函数保持一致
    def inner(*args):
        return f(*map(float, args))

    return inner


# 装饰器函数，转为正值
def format_abs(f):
    def inner(x):
        return f(abs(x))

    return inner


# 装饰器函数，保留2位小数
def format_round2(f):
    def inner(x):
        return round(f(x), 2)

    return inner


# 多个装饰器顺序：
# @a
# @b
# a 处理参数 => b 处理参数 => 原函数 => b处理返回值 => a 处理返回值
@format_float
@format_abs
@format_round2
def sqrt(x):
    return x ** 0.5


print(sqrt("-10"))


@format_float
def add(a, b):
    return a + b


print(add("1", "2"))
