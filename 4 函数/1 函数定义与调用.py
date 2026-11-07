# 定义函数
def say_hello():
    print("hello world")


# 调用函数，函数不调用不会执行
# 函数必须先定义后使用，python 不会把函数作用域提升
# python 没有函数重载，名字相同直接覆盖
say_hello()


def a():
    print("a")
    # 这里先定义了a函数但不执行，b的执行还是在b函数定义之后
    b()

def b():
    print("b")

a()