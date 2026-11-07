# 使用单引号或双引号包裹表示单行字符串
str1 = "hello world"

# 使用三个单引号或三个双引号包裹表示多行文本，可以保留换行符号
str2 = """hello
world"""
print(str2)

# 支持不同引号嵌套，但相同引号不能嵌套
str1 = "he says 'hello'"
print(str1)
str2 = 'he says "hello"'
print(str2)

# 转义字符
# \n 换行
# \r 光标回到行首，且输出会覆盖已有内容
# \t 制表
# \\ 斜杠本身
# \" 双引号
# \' 单引号
str1 = "he says \"hello\""
print(str1)
str2 = "D:\\demo1\\file.txt"
print(str2)
str3 = "hello\nworld"
print(str3)

# r 表示原始字符串，不转义
str1 = r"D:\demo\file.txt"
print(str1)

# 字符串也有字符串池（要求字符串不含空格、制表、回车等空白符）
str1 = "hello"
str2 = "hello"
print(id(str1) == id(str2))
# 含空白符的字符串 PyCharm 和非 PyCharm 环境执行会有不同效果
str1 = "hello world"
str2 = "hello world"
print(id(str1) == id(str2))

# 字符串拼接（只支持字符串与字符串拼接）
str1 = "hello" + "world"
print(str1)
# 其它类型和字符串拼接必须强转
str2 = "123" + str(456)
print(str2)

# 编码解码（编码和解码字符集必须一致，一般都使用 utf-8）
# 编码：字符串 => 二进制字节串
# 解码：二进制字节串 => 字符串
origin_str = "你好"
bytes = origin_str.encode("utf-8")
print(bytes)
decoded_str = bytes.decode("utf-8")
print(decoded_str)

# 单个字符 <=> ASCII编码值
# '0' <=> 48
# 'A' <=> 65
# 'a' <=> 97
code = ord('a')
print(code)
letter = chr(65)
print(letter)
