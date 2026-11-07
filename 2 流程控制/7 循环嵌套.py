import math

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}", end="\t")
    print()

# 打印三角形
#   *
#  ***
# *****
# ...
n = 5
for i in range(n):
    strip_num = n - i - 1
    start_num = 2 * i + 1
    line = " " * strip_num + "*" * start_num + " " * strip_num
    print(line)

# 找到 1~100以内所有完数，完数=它所有因子和（不含本身），比如 6=1+2+3
for i in range(1, 101):
    factor_sum = 0
    for j in range(1, i):
        if i % j == 0:
            factor_sum += j
            if factor_sum > i:
                break
    if factor_sum == i:
        print(i, end=" ")
else:
    print()

# 找出[1, 100]内所有质数
for i in range(2, 101):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
else:
    print()
