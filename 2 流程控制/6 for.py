# for 变量 in 可迭代对象
# 遍历可迭代对象，知道次数，使用 for 循环
# 如果只知道循环终止条件，使用 while 循环

# 遍历字符串
word = "hello world"
for letter in word:
    print(letter, end=" ")
# 正常结束循环会进入 else
else:
    print()

# 遍历 range(start, end, step) 从 start（包含）到 end（不包含）步长为 step
# 0, 1, 2, 3, 4
for item in range(5):
    print(item, end=" ")
else:
    print()
# 1, 3, 5, 7, 9
for item in range(1, 10, 2):
    print(item, end=" ")
else:
    print()
# 10, 8, 6, 4, 2
for item in range(10, 1, -2):
    print(item, end=" ")
else:
    print()
# 求 1-100 所有奇数和
sum_val = 0
for item in range(1, 100, 2):
    sum_val += item
print(sum_val)
