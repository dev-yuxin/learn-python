import random

# break 中断循环
# 产生一个 [1, 100] 的随机整数
num = random.randint(1, 100)
while True:
    guess = int(input("猜一个[1, 100]的整数"))
    if guess == num:
        print("猜对了")
        break
    elif guess < num:
        print("小了")
    else:
        print("大了")

# continue 后面语句不执行，跳过本次循环，继续下一次循环
# 输出 1~10 跳过 3 的倍数
num = 0
while num <= 10:
    if num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1

# pass 占位，避免报错
if True:
    pass
