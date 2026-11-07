# bool 类型只有两个值，True 和 False（注意大小写）
flag = True
if flag:
    print("条件成立")
else:
    print("条件不成立")

# 0, 0.0, 空字符串, 空列表, 空元组, 空集合, 空字典等表示空的值会被自动转换为 False
# 非空的值会被自动转换为 True
a = 0.0
if a:
    print("非空")
else:
    print("空")

# bool 是 int 的子类型
print(isinstance(True, int))
