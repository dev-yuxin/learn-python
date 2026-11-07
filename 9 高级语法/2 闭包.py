def f():
    a = 1


f()


# 当f执行完后释放，外面自然无法访问 a
# print(a)


# 闭包就是函数能记住它定义时的环境，即使这个环境被释放，也能继续访问这个环境里的变量。
def outer():
    b = 2

    def inner():
        print(b)

    return inner


inner_f = outer()
# 虽然 outer 执行完后释放了，我们在外面访问不了b。但是闭包机制把 b 记录到 inner_f 中，inner_f 中能继续访问b。
for item in inner_f.__closure__:
    print(item.cell_contents)
inner_f()
