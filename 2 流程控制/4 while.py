# 有一个内置 sum 函数，标识符不要重名
sum_num = 0
i = 1
while i <= 100:
    sum_num += i
    i += 1
# 循环正常结束会进入 else ，break 或异常等非正常结束则不会进入 else
else:
    print("循环正常结束")
print(f"{sum_num=}, {i=}")
