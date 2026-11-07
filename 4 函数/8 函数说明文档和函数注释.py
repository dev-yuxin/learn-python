# 函数注释，说明参数和返回值类型
def add(a: int, b: int) -> int:
    """
    函数说明文档，以下是 Google-Style 风格的函数说明文档
    求2个整数的和

    Args:
        a: 第一个整数
        b: 第二个整数

    Return:
        和
    """
    return a + b


# 函数说明文档 和 函数注释起到更好的提示作用
# 这是一种约定，不是强制
print(add(1, 2))
