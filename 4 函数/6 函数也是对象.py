# python 中函数也是对象
# 就像 1 是 int 类型的对象，它能干的操作函数也能干
# 赋值给变量
# 定义在函数体中
# 作为函数参数
# 作为函数返回值
# 放在容器中
# ...


def f1():
    print("f1")


# 把函数对象赋值给f1，注意不要加()，加()是函数调用把返回值赋值给f2
f2 = f1
f2()

# 函数作为参数传递
list1 = ["hello", "world", "python", "llm"]
list1.sort(key=len)
print(list1)


# 函数可以定义在函数体里，也可以作为返回值
def calculate(sign):
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match sign:
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div
        case _:
            return add


print(calculate("+")(1, 2))

# 函数存放在容器里
dict1 = {
    "+": calculate("+"),
    "-": calculate("-"),
    "*": calculate("*"),
    "/": calculate("/"),
}
print(dict1["+"](1, 2))
