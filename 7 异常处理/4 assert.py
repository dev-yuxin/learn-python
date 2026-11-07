# assert 用于测试验证，如果后面表达式为 False，抛出一个 AssertionError
try:
    assert 1 + 1 == 2
    print("计算正确")
except AssertionError as e:
    print(e)

try:
    assert 1 + 1 == 3, "计算错误"
except AssertionError as e:
    print(e)
