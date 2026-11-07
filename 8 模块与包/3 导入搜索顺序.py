# 1 sys.modules（已导入模块的缓存）
# 2 BuiltinImporter（内置模块，比如 os, math 等等）
# 3 FrozenImporter（冻结模块，一般用不到）
# 4 sys.path（默认按照 当前目录 => 项目根目录 => python安装目录 => venv目录）
# 5 没找到报错

import sys

print(sys.path)
