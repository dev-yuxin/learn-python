# return 用于返回值，表示函数结束，后面代码无效

def say_hello():
    print("hello")
    # 不写return语句返回None


def say_hello2():
    print("hello")
    return
    # 只写return不写值，返回None


def add(a, b):
    return a + b
    # 返回指定值


def calculate(a, b):
    return a + b, a - b, a * b, a / b
    # 返回多个值，是一个元组


print(say_hello())
print(say_hello2())
print(add(1, 2))
print(calculate(1, 2))
