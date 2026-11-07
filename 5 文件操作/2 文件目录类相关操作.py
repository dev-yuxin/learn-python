import os
import shutil

# 获取文件大小（字节） 只能获取文件大小，目录大小不准确
print(os.path.getsize("assets/1.txt"))
# 获取文件或目录创建时间（ms时间戳）
print(os.path.getctime("assets/1.txt"))
# 获取文件或目录最后访问时间（ms时间戳）
print(os.path.getatime("assets/1.txt"))
# 获取文件或目录最后修改时间（ms时间戳）
print(os.path.getmtime("assets/1.txt"))

# 判断路径是否是文件
print(os.path.isfile("assets/1.txt"))
# 判断路径是否是目录
print(os.path.isdir("../5 文件操作"))
# 判断路径是否有效
print(os.path.exists("../5 文件操作"))

# 获取绝对路径
print(os.path.abspath("."))
print(os.path.abspath("assets/1.txt"))
# 获取路径中的文件名（包含文件名前缀后缀，不含所在目录）
print(os.path.basename("assets/1.txt"))
# 获取路径中的目录，如果没有则返回空字符串
print(os.path.dirname("1.txt"))
print(os.path.dirname(os.path.abspath("assets/1.txt")))
# 获取 (dirname, basename) 的元组
print(os.path.split(os.path.abspath("assets/1.txt")))
# 获取 (dirname+basename前缀不含.xxx, basename后缀.xxx)
print(os.path.splitext(os.path.abspath("assets/1.txt")))

# 路径拼接（兼容不同系统）
print(os.path.join(os.path.abspath("."), "2.txt"))

# 获取工作区的绝对路径
print(os.getcwd())

# 创建目录（目录已存在会报错）
if not os.path.isdir("test"):
    os.mkdir("test")
# 创建多级目录（目录已存在会报错）
if not os.path.isdir("test/one/1-1"):
    os.makedirs("test/one/1-1")
if not os.path.isdir("test/two/2-1"):
    os.makedirs("test/two/2-1")

# 创建文件（如果已存在则覆盖写）
if not os.path.isfile(r"test/one/1-1/a.txt"):
    open(r"test/one/1-1/a.txt", "wt", encoding="utf-8").close()
if not os.path.isfile(r"test/two/2-1/b.txt"):
    open(r"test/two/2-1/b.txt", "wt", encoding="utf-8").close()

# 复制文件（如果已存在会覆盖）
shutil.copy2(r"test/one/1-1/a.txt", r"test/one/1-1/b.txt")
# 复制整个目录（目录已存在会报错）
if not os.path.isdir(r"test/one/1-2"):
    shutil.copytree(r"test/one/1-1", r"test/one/1-2")

# 删除文件
if os.path.isfile(r"test/one/1-1/a.txt"):
    os.remove(r"test/one/1-1/a.txt")
if os.path.isfile(r"test/one/1-1/b.txt"):
    os.remove(r"test/one/1-1/b.txt")
if os.path.isfile(r"test/one/1-2/a.txt"):
    os.remove(r"test/one/1-2/a.txt")
if os.path.isfile(r"test/one/1-2/b.txt"):
    os.remove(r"test/one/1-2/b.txt")

# 删除一级空目录
if os.path.isdir(r"test/one/1-1"):
    os.rmdir(r"test/one/1-1")

# 删除多级空目录
if os.path.isdir(r"test/one/1-2"):
    os.removedirs(r"test/one/1-2")

# 递归删除目录（慎用）
# shutil.rmtree(path)

# 移动/重命名 文件/目录（如果源不存在以及目标已存在会报错）
# os.rename() 不能跨盘符
# shutil.move() 能跨盘符
if os.path.isdir(r"test/two/2-1") and not os.path.isdir(r"test/2-1"):
    os.rename(r"test/two/2-1", r"test/2-1")
    os.rename(r"test/2-1/b.txt", r"test/2-1/a.txt")

# 查看目录下有哪些文件和子目录，返回文件名和目录名组成的列表（只有一层，不会递归）
print(os.listdir("."))

# 递归查看目录下有哪些文件和子目录，返回一个迭代器
# 每次遍历得到一个三元组 (dirname, [子目录列表], [子文件列表])
for dirname, sub_dir_list, sub_file_list in os.walk("."):
    for item in sub_dir_list:
        print(os.path.join(dirname, item))
    for item in sub_file_list:
        print(os.path.join(dirname, item))
