import decimal

# float 表示浮点型，只能得到近似值
num1 = 0.1
num2 = 0.2
print(num1 + num2)

# 科学计数法
num1 = 1.5e10
print(num1)

# round 可以控制精确到小数点后几位
# python 中四舍，五如果向下取整是偶数则舍，向上取整是偶数则入
num1 = 0.5555
num2 = round(num1, 2)
print(num2)
num3 = round(2.55, 1)
print(num3)

# 如果涉及金钱类计算，使用 Decimal
num1 = decimal.Decimal("0.1")
num2 = decimal.Decimal("0.2")
print(num1 + num2)
