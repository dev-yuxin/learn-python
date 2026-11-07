# 一个 .py 文件就是一个模块，里面会有类、函数、变量等

# 方式一
# import 模块名 [as 别名]
# 所有成员都能用，包括私有和不在__all__中的，只是不推荐使用
import calc
import seq

print(calc._msg1)
print(calc.add(123, 4))

print(seq._msg2)
print(seq.add("123", "4"))

# 方式二
# from 模块 import 成员 [as 别名]
# 所有成员都能导入，包括私有和不在__all__中的，只是不推荐使用
# 同名后面的覆盖前面的，需要手动使用 as 解决
from calc import _msg1
from calc import add
from seq import _msg2
from seq import add as seq_add

print(_msg1)
print(add(123, 4))
print(_msg2)
print(seq_add("123", "4"))

# 方式三
# from 模块 import *
# * 表示全部，如果模块中定义了 __all__ 则 * 为 __all__ 中的成员，如果没有定义 __all__ 则 * 为所有非私有成员
# 同名冲突后面的覆盖前面的，需要使用方式二单独导入并使用 as 起别名
from vector import *
from vector import add as vec_add

# print(_msg3)  # 没有导入 _msg3 会报错
print(vec_add((1, 2, 3), (4, 5, 6)))
print(mul((1, 2, 3), (4, 5, 6)))
