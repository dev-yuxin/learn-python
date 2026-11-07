# 带参数的装饰器函数，保留n位小数
# 最外层函数参数是装饰器的参数
def format_round(n):
    # 中间层函数参数接收一个函数
    def middle(f):
        # 最内层函数参数和原函数保持一致
        def inner(x):
            return round(f(x), n)

        return inner

    return middle


@format_round(2)
def sqrt(x):
    return x ** 0.5


print(sqrt(10))
