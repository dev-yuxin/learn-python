import random

# 随机产生一个 [0, 1) 的浮点数
print(random.random())

# 随机产生一个 [10, 100] 的浮点数
print(random.uniform(10, 100))

# 随机产生一个 [10, 100] 的整数
print(random.randint(1, 10))

# 随机打乱
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)
random.shuffle(nums)
print(nums)
