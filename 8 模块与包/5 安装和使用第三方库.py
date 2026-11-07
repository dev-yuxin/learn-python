# 打开终端，使用 pip 安装
# 如果不在项目下，将安装到 python 的安装目录下（除非你确定是要全局使用）。
# 如果在项目中且激活 venv ，将安装到项目的 venv 虚拟环境下（推荐，不会污染环境）。

"""
pip 常用命令

# 永久修改镜像源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 安装指定包（最新版）
pip install <包名>

# 安装包指定版本
pip install <包名==版本号>

# 根据 requirements.txt 文件批量安装
pip install -r requirements.txt

# 临时使用镜像源安装
pip install -i https://mirrors.aliyun.com/pypi/simple/ <包名>

# 删除包
pip uninstall <包名>
"""

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
