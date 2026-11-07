# open()
# 第一个参数是路径，可以是绝对路径，也可以是相对路径
# 第二个参数是模式
# r: 读模式，文件不存在会报错
# w: 覆盖写模式，文件不存在会自动创建
# a: 追加写模式，文件不存在会自动创建
# t: 纯文本文件（如果是纯文本文件，需要使用 encoding 指定字符编码）
# b: 二进制文件

# 纯文本文件覆盖写
f = open(r"assets/1.txt", "wt", encoding="utf-8")
# write() 将字符串或字节串写入文件，要自己加换行符
f.write("hello")
f.write("world\n")
f.write("123\n")
# 不要忘记关了
f.close()

# 纯文本文件追加写
# 你也可以使用 with 这样能自动关闭
with open(r"assets/1.txt", "at", encoding="utf-8") as f:
    f.write("llm\n")
    f.write("python\n")
    f.close()

# 纯文本文件读
with open(r"assets/1.txt", "rt", encoding="utf-8") as f:
    # 一次读取全部
    all_content = f.read()
    print(all_content)

# 纯文本文件读
with open(r"assets/1.txt", "rt", encoding="utf-8") as f:
    # 每次读3个字符
    while content := f.read(3):
        print(content, end="")
    print()

# 纯文本文件读
with open(r"assets/1.txt", "rt", encoding="utf-8") as f:
    # 每次只读一行（包含换行符）
    while line := f.readline():
        print(line, end="")
    print()

# 纯文本文件读
with open(r"assets/1.txt", "rt", encoding="utf-8") as f:
    # 每次只读一行（包含换行符）
    # 等价于上面写法
    for line in f:
        print(line, end="")
    print()

# 纯文本文件读
with open(r"assets/1.txt", "rt", encoding="utf-8") as f:
    # 将每行（包括换行符）组成一个列表
    lines = f.readlines()
    print(lines)


# 二进制文件的读写
def copy_file(src, dst, size=1024):
    with open(src, "rb") as fr, open(dst, "wb") as fw:
        while content := fr.read(size):
            fw.write(content)


copy_file("assets/1.jpg", "assets/2.jpg")
