_msg1 = "四则运算"


def add(num1, num2):
    """普通加法"""
    return num1 + num2


def mul(num1, num2):
    """普通乘法"""
    return num1 * num2


print(f"加载{_msg1}模块")

if __name__ == "__main__":
    print(add(1, 2))
