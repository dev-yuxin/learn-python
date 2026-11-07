# 函数嵌套调用，栈结构
def a():
    print("a函数开始执行")
    b()
    print("a函数执行完毕")


def b():
    print("b函数开始执行")
    c()
    print("b函数执行完毕")


def c():
    print("c函数开始执行")
    print("c函数执行完毕")


a()


# 如果函数调用的是自身（可以是直接调用自身，也可以间接调用自身），则称为递归调用
# 递归一定要有终止条件

# 递归求阶乘
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))


# 递归求斐波那契数列
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


# 递归求汉诺塔
def hanoi(n, column_resource, column_target, column_help):
    if n <= 1:
        # 只有一个直接从 resource -> target
        print(f"{column_resource} -> {column_target}")
        return
    else:
        # 先把 n-1 个从 resource -> help 借助 target
        hanoi(n - 1, column_resource, column_help, column_target)
        # 再把底下第 n 个从 resource -> target
        print(f"{column_resource} -> {column_target}")
        # 再把 n-1 个从 help -> target 借助 resource
        hanoi(n - 1, column_help, column_target, column_resource)


hanoi(5, "a", "b", "c")
