# 包用来管理模块的
# 包和普通目录的区别在于，有一个 __init__.py

# 方式一（导入到包）
# import 包名[.子包名] [as 别名]
import my_pkg

# 导入时只导入到某个包，使用时要从该包下找，需要在该包的 __init__.py 中声明非私有名字，一般会使用 from . import 名字
# 如果导入时包下面的路径已经用`.`指明，使用时则不需要在该包的 __init__.py 中声明非私有名字
print(my_pkg.pkg1.seq.add("123", "4"))

# 方式二（导入到模块）
# import 包[.子包].模块 [as 别名]
# from 包[.子包] import 模块 [as 别名]
# from 包[.子包] import *
# * 表示所有模块时，优先看 __init__.py 文件的 __all__ ，没有就看 __init__.py 里有哪些非私有名字
import my_pkg.pkg2.calc
from my_pkg.pkg2 import *
from my_pkg.pkg2 import vector as vec

# 导入的是 my_pkg.pkg2.calc 就必须写完整，或者起个别名
print(my_pkg.pkg2.calc.add(1, 2))
print(vector.add((1, 2), (3, 4)))
print(calc.add(1, 2))
print(vec.add((1, 2), (3, 4)))

# 方式三（导入到成员）
# 规则同模块的规则
# from 包[.子包].模块 import 成员 [as 别名]
# from 包[.子包].模块 import *
from my_pkg.pkg2.calc import *

print(add(1, 2))

# 注意事项：
# 单 import 语句必须以包或模块结束，不能是成员。from-import 语句则都可以。
# `.` 在导入语句中只能用于`包.子包`, `包.模块`，不能用于`模块.成员`。非导入语句中允许`模块.成员`。