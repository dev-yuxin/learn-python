import re

# 正则表达式
# ^           匹配开始字符
# $           匹配结束字符
# .           匹配任一一个字符
# \d          匹配一个数字字符
# \D          匹配一个非数字字符
# \s          匹配一个空白字符
# \S          匹配一个非空白字符
# \w          匹配一个文本字符（英文字母or数字or下划线）
# \W          匹配一个非文本字符
# [abc123]    匹配 a,b,c,1,2,3 中的一个字符
# [a-z]       匹配 a,b,c,...,z 中的一个字符
# \d*         匹配 0 个或 1 个数字字符
# \d+         匹配 >=1 个数字字符（默认贪心匹配，比如123会直接匹配全部）
# \d?         匹配 0 或 1 个数字字符
# \d{3}       匹配 3 个数字字符
# \d{3,}      匹配 >=3 个数字字符
# \d{3,5}     匹配 3 到 5（包含边界）个数字字符
# |           或运算
# ()          捕获组
# 特殊字符需使用 \ 转义

phone = input("请输入手机号：")
# re.match() 匹配整个文本，正则需要加 ^$
# 如果匹配成功返回一个 match 对象，匹配失败返回 None
if re.match(r"^1[3-9][0-9]{9}$", phone):
    print("手机号校验通过")
else:
    print("手机号错误")

text = "Python-123java456 llm"

# re.search() 搜索，从左往右搜索，搜索到首个就停止
# 找到返回一个 match 对象，没找到返回 None
result = re.search(r"[a-z]+", text, flags=re.I)  # re.I 表示忽略大小写
if result:
    print(f"已找到：{result.group()}，索引：[{result.start()}, {result.end()})")
else:
    print("未找到")

# re.findall() 搜索全部，将匹配的文本组成字符串列表返回
result = re.findall(r"[a-z]+", text, flags=re.I)
print(result)

# re.finditer() 搜索全部，返回一个可迭代对象
# 你可以通过 item.start(), item.end(), item.group() 获取相关信息
result = [(item.group(), item.start(), item.end()) for item in re.finditer(r"[a-z]+", text, flags=re.I)]
print(result)

# str.replace() 只能传入字符串
# re.sub() 可以传入正则
new_str = re.sub(r"[a-z]", "*", text, flags=re.I)
print(new_str)

# str.split() 只能传入字符串
# re.split() 能传入正则
text = "a,b;c.:  d"
list1 = re.split(r"[,;.:\s]+", text)
print(list1)

# 捕获组（匹配左括号）
text = "2026年5月01日是劳动节。"
reg = r"(\d{4})年0?([1-9]|1[0-2])月0?([1-9]|[12]\d|3[01])日"
result = re.search(reg, text)
if result:
    # group(0) 或者 group() 是完整的匹配内容
    print(f"匹配到的完整内容: {result.group()}")
    print(f"第1个捕获组: {result.group(1)}")
    print(f"第2个捕获组: {result.group(2)}")
    print(f"第3个捕获组: {result.group(3)}")
