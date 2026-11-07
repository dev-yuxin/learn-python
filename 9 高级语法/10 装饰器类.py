# 装饰器类也能实现装饰器的功能

# 不带参数的装饰器写法一，对应装饰器 @FormatFloat()
class FormatFloat:
    def __call__(self, f):
        def inner(x):
            return f(float(x))

        return inner


# 不带参数的装饰器写法二，对应装饰器 @FormatAbs
class FormatAbs:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        return self.f(abs(x))


# 带参数只能这么写，对应装饰器 @FormatRound(n)
class FormatRound:
    def __init__(self, n):
        self.n = n

    def __call__(self, f):
        def inner(x):
            return round(f(x), self.n)

        return inner


@FormatFloat()
@FormatAbs
@FormatRound(2)
def sqrt(x):
    return x ** 0.5


print(sqrt("-10"))
