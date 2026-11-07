import string

# 创建字符串，一般都使用字面量创建
str1 = "hello"
str2 = ""

# 将其它对象转为字符串
str3 = str(123)

# 字符串是不可变的，函数不会动原字符串，返回一个新字符串

# replace(old, new) 把所有old替换为new，返回一个新字符串
str1 = "hello"
str2 = str1.replace("l", "L")
print(str2)
# 指定替换最大次数
str3 = str1.replace("l", "L", 1)
print(str3)

# split() 默认用空白符分割，返回一个字符串列表
str1 = "hello world     python"
list1 = str1.split()
print(list1)
# 指定分隔符
str2 = "hello,world,python"
list2 = str2.split(",")
print(list2)

# join() 把可迭代对象（要求每个元素是字符串）按指定字符串拼接，返回一个字符串
list1 = [1, 2, 3, 4, 5]
str1 = ",".join([str(item) for item in list1])
print(str1)

# strip() 去掉前后字符，默认是空白符，返回新字符串
str1 = " hello world "
print(str1.strip())
# 去掉指定字符
str2 = "***abc*"
print(str2.strip("*"))
# 只去掉左边
print(str2.lstrip("*"))
# 只去掉右边
print(str2.rstrip("*"))

# upper() 全部转大写
# lower() 全部转小写
# capitalize() 首字母大写，其它小写
# title() 每个单词（非单词字符视为分割符）首字母大写，其它小写
# swapcase() 大写转小写，小写转大写
str1 = "HELLO world"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.title())
print(str1.swapcase())

# 查找
# index()
str1 = "hello world"
print(str1.index("l"))
print(str1.index("l", 6, -1))
print(str1.index("l", 6))
# 字符串新增了 rindex(), find(), rfind()
# rindex() 查找顺序从右往左查
print(str1.rindex("l"))
print(str1.rindex("l", 6, -1))
print(str1.rindex("l", 6))
# find() 和 rfind() 和 index() rindex() 区别
# index() 和 rindex() 找不到报错
# find() 和 rfind() 找不到返回 -1
print(str1.find("l"))
print(str1.rfind("l", -3, 4))

# 判断是否以xxx开头或结尾
str1 = "张三"
print(str1.startswith("张"))
str2 = "file1.py"
print(str2.endswith(".py"))

# 判断字符串内容是否满足条件
# isalpha() 只文字字符（英文字母、中文汉字、日语韩语等）
# isascii() 字符是否全全在ascii表里
# 可以使用 isalpha() and isascii() 判断字符串是否只含英文字母
str1 = "hello world"
print(str1.isalpha() and str1.isascii())
# isdecimal() 是否只含（0~9）
# isdigit() 是否只含（0~9）、角标数字
# isnumeric() 是否只含数字（0~9）、角标数字、罗马数字、中文数字等
print("123".isdecimal())
print("2²".isdigit())
print("一".isnumeric())
# string.ascii_leter 表示英文大小写字母组成的字符串
# string.ascii_uppercase 表示英文大写字母组成的字符串
# string.ascii_lowercase 表示英文小写字母组成的字符串
# string.digits 表示0~9组成的字符串
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)

# 字符串填充 ljust(), rjust(), center(), zfill()
# 你也可以使用 {:}
# 默认使用空格填充
print("123".center(10))
print(f"{'123':^10}")
# 指定字符填充
print("123".ljust(10, "*"))
print(f"{'123':*<10}")
print("123".rjust(10, "*"))
print(f"{'123':*>10}")
# 左边补0
print("123".zfill(10))
