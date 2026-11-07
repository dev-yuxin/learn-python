# 自动转换
# bool => int => float
num1 = True + 1.0
print(num1, type(num1))
# 除法除得进也转为 float 型
num2 = 2 / 1
print(num2, type(num2))

# 自动转换
# 条件判断 => bool
list1 = []
if list1:
    print("列表非空")
else:
    print("列表为空")

# 强制类型转换（转换不通过会报错）
num1 = 1
str1 = "123"
print("求和", num1 + int(str1))
print("拼接", str(num1) + str1)
