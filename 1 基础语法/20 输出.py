# print() 将内容输出到控制台，底层会调用 __str__()
# 输出一个参数
print(1)

# 输出多个参数，分隔符默认用空格，结束符默认用\t
print("a =", 1, "b =", 2, "c =", 3)
# 指定分隔符和结束符
print("a = 1", "b = 2", "c = 3", sep=",", end="\t")

name = "tom"
age = 18
salary = 15000.966
r = 1
pi = 3.1415926

# 字符串的格式化
# "%d %s %f"%()
# 参数要和占位符一一对应
# %d 十进制int型
# %s str型
# %f float型
# %.2f float型保留2位小数
print("name: %s, age: %d, salary: %.2f" % (name, age, salary))

# 字符串的格式化
# "{} {} {}".format()
# 参数和占位符一一对应
print("name={}, age={}, salary={}".format(name, age, salary))
# 参数和位置一一对应
print("交换前 x={0}, y={1} 交换后 x={1}, y={0}".format(1, 2))
# 关键字参数和别名一一对应
print("name={my_name}, age={my_age}, salary={my_salary}".format(my_name=name, my_age=age, my_salary=salary))

# 字符串的格式化
# f"{变量}"
# 直接把变量赋值给占位符，等价于 "name={name}, age={age}, salary={salary}".format(name=name, age=age, salary=salary)
print(f"name={name}, age={age}, salary={salary}")
# 简写，自动填入
print(f"{name=}, {age=}, {salary=}")

# {} 中的格式控制
# {:.2f} 保留小数点后2位
print("r={}, area={:.2f}".format(r, pi * r * r))
print("r={0}, area={1:.2f}".format(r, pi * r * r))
print("r={r}, area={area:.2f}".format(r=r, area=pi * r * r))
print(f"{r=}, area={pi * r * r:.2f}")
# {:>10d} 整数拓展到10位，右对齐，左边空格填充
# {:*<10s} 字符串拓展到10位，左对齐，右边用*填充
# {:*^10s} 字符串拓展到10位，居中对齐，左右两边用*填充
print(f"{age:0>3d}")
print(f"{name:*^10s}")
# {:.2%} 转成百分比，保留2位小数
print(f"{0.186726:.2%}")
